from os import _exit
from signal import signal, SIGINT
from threading import Thread
from PIL import Image, ImageTk, ImageDraw, ImageEnhance
from tkinter import filedialog, Tk, Frame,\
        Label, Button, Scale, IntVar, DISABLED, HORIZONTAL

# FUNCTION
# ================================================
def handler(sig, frm): _exit(0)

def invalid_input(info):
    print(f"\033[31mInvalid input: {info}.\033[0m")
    _exit(0)

def meanless_input(var, text):
    print(f"Meanless input: {var}.")
    print(f"The {text} won't change.")

def img_info():
    print("\033[36m==================Info==================\033[0m")
    print(f'\033[36mPath: {file}\033[0m')
    if old_mode:
        print(f'\033[36mMode: {old_mode} <-> {img.mode}\033[0m')
    else:
        print(f'\033[36mMode: {img.mode}\033[0m')
    print(f'\033[36mResolution: {img.size[0]}px, {img.size[1]}px\033[0m')

def file_analysis(f):
    # If user clicked cancel or hit esc,
    # show message instead of error msg.
    if f in [(), '.', '']:
        print("\033[36mNothing input, quitting now.\033[0m")
        _exit(0)
   
def ftype_analysis(f, ftype):
    # If the input file is not a graph file,
    # throw the error.
    if ftype not in support_files: invalid_input(f)

def exec_crop():
    global t1
    t1 = Thread(target=crop_active,
                args=(new_img_xl.get(),
                      new_img_yt.get(),
                      tk_s_img_x-new_img_xr.get(),
                      tk_s_img_y-new_img_yb.get()))
    t1.start()
    threads.append(t1)

def exec_restore():
    global t2
    t2 = Thread(target=restore,
                args=(new_img_xl, new_img_yt,
                      new_img_xr, new_img_yb))
    t2.start()
    threads.append(t2)

def draw_section(x, y, x1, y1, fac):
    rect = [( round(x/fac), round(y/fac) ),
            ( round(x1/fac), round(y1/fac) )]
    crop_section_img = ImageDraw.Draw(tk_prev_img)
    crop_section_img.rectangle(rect, fill=None, outline="black")

def refresh_image(get, show, prev):
    get = ImageTk.PhotoImage(prev)
    show.configure(image=get)
    show.image = get

def crop_active(x, y, x1, y1):
    global count, tst_img, tk_prev_img

    new_img = (x, y, x1, y1)
    # If the crop position is correct, it'll work
    if x < x1 and y < y1:
        # If the scale's value changed, it'll work
        if (x or y)!=0 or \
        x1 != tk_s_img_x or y1 != tk_s_img_y:
            tst_img = sharpened_img.crop(new_img)

            if count != 0:
                count = 0
                # Reset the preview image
                tk_prev_img = sharpened_img.resize(
                        (tk_prev_img_x, tk_prev_img_y),
                        resample=Image.BILINEAR)
            count = 1
            draw_section(*new_img, tk_img_factor)
            refresh_image(tk_get_image, tk_show_image, tk_prev_img)
            tst_img.show()

            # Change the text.
            tk_text_r.configure(text=text_r(tst_img.size[0], tst_img.size[1], "(Cropped)"))
            tk_close_button.configure(text="Save 2 images.")
    else: invalid_input(new_img)

def restore(x, y, x1, y1):
    global count, tst_img, tk_prev_img
   
    # Clear various stuff
    count = 0
    tst_img = None
    for i in x, y, x1, y1: i.set(0)
    
    # Refresh the image
    tk_prev_img = sharpened_img.resize(
            (tk_prev_img_x, tk_prev_img_y),
            resample=Image.BILINEAR)
    refresh_image(tk_get_image, tk_show_image, tk_prev_img)
    
    tk_text_r.configure(text=text_r(tk_s_img_x, tk_s_img_y, ""))
    tk_close_button.configure(text="Close")

def close_active():
    for t in threads: t.join()
    root.destroy()

def save_file(img, fname, f_ext, text):
    if fname in ['/', '\\', '*', ':', '?',
                 '|', '<', '>', '.', '..']:
        print(f"Avoid character {fname}.")
        fname="output"
    if old_mode: img.convert(old_mode)
    img.save(f'{fname}{text}.{f_ext}')
    print(f"\033[32m{fname}{text}.{f_ext}, output successfully.\033[0m")
# ================================TheEndOfFunction



# VARIABLE
# ================================================
signal(SIGINT, handler)

support_files=["png", "jpg", "bmp", "gif",
               "tif", "webp", "ico", "psd"]

value_invalid="value not allowed"

print("\033[36mPlease select an image.\033[0m")
print(f"\033[36mSupport images are {support_files}.\033[0m")

file = filedialog.askopenfilename()
file_analysis(file)
file_short_name = file.split("/")[-1]
file_extension = ((file_short_name).split("."))[-1]
ftype_analysis(file, file_extension)

_e = Exception

threads = []

# If it's ok, then open the image.
img = Image.open(file)
tst_img = None

old_mode = None
if img.mode not in ["RGB", "RGBA"]:
    old_mode = img.mode
    img=img.convert("RGBA")
# ================================================



# MAIN
# ================================================
img_info()

# Graph's resolution
manual_or_keep=input("手动输入分辨率大小(m)还是保持长宽比(k): ")
if manual_or_keep in ['m', 'M']:
    try: m_image_x = int(input("请输入长: "))
    except _e: invalid_input(value_invalid)
    try: m_image_y = int(input("请输入宽: "))
    except _e: invalid_input(value_invalid)

    m_resolution = (m_image_x, m_image_y)

    # It's not necessary to resize image which has
    # the same size of the origin one.
    if m_resolution != img.size and \
    (m_image_x and m_image_y) > 0:
        resized_img = img.resize(m_resolution, resample=Image.BILINEAR)
    else: meanless_input(m_resolution, "resolution")
elif manual_or_keep in ['k', 'K']:
    try: k_value=float(input("请输入缩放图片的倍率(... 0.5, 2, 5 ...): "))
    except _e: invalid_input(value_invalid)
    k_image_x = round(img.size[0]*k_value)
    k_image_y = round(img.size[1]*k_value)

    k_resolution = (k_image_x, k_image_y)

    if k_value != 1 and k_value > 0:
        resized_img = img.resize(
            k_resolution, resample=Image.BILINEAR)
    else:
        resized_img = img
        meanless_input(k_value, "resolution")
else: invalid_input(manual_or_keep)

# Graph's sharpness
sharpen_or_not=input("锐化(y/n): ")
if sharpen_or_not in ['y', 'Y']:
    if img.mode not in ["RGB", "RGBA"]: img.convert("RGB")
    sharpen_tool=ImageEnhance.Sharpness(resized_img)
    
    try: sharpness = float(input("输入锐化因子(默认值2): "))
    except _e: invalid_input(value_invalid)

    if sharpness >= 0:
        sharpened_img = sharpen_tool.enhance(sharpness)
    else: meanless_input(sharpness, "sharpness")
else: sharpened_img = resized_img
# ================================================



# GUI
# ================================================
root = Tk()
root.title("Image preview")
root.resizable(0, 0)

count = 0

new_img_xl = IntVar()
new_img_xr = IntVar()
new_img_yt = IntVar()
new_img_yb = IntVar()

text_r = lambda x, y, text: f"Resolution{text}: {x}px, {y}px"

# Get the size of the image.
tk_s_img_x = sharpened_img.size[0]
tk_s_img_y = sharpened_img.size[1]
tk_img_factor = max(tk_s_img_x/448, tk_s_img_y/336)

# The preview image's size should be smaller.
tk_prev_img_x = round(tk_s_img_x/tk_img_factor)
tk_prev_img_y = round(tk_s_img_y/tk_img_factor)
tk_prev_img_resolution = (tk_prev_img_x, tk_prev_img_y)
tk_prev_img = sharpened_img.resize(
        tk_prev_img_resolution, resample=Image.BILINEAR)

# Settings
# Objects
# ================================================
# Image section
tk_main_frame = Frame(root)

# Image info
tk_content_frame = Frame(tk_main_frame)
tk_get_image = ImageTk.PhotoImage(tk_prev_img)
tk_text_image = Label(tk_content_frame, height=1,
                      text="Preview image")
tk_show_image = Label(tk_content_frame, image=tk_get_image,
                      borderwidth=1, relief="solid")
tk_text_r = Label(tk_content_frame, height=1,
                  text=text_r(tk_s_img_x, tk_s_img_y, ""))

# Crop-Y section
tk_cropy_frame = Frame(tk_main_frame)
tk_text_cropyt = Label(tk_cropy_frame, height=1, text="Crop top:")
tk_scale_yt = Scale(tk_cropy_frame, variable=new_img_yt,
                    resolution=1, borderwidth=1,
                    from_=0, to=tk_s_img_y-1, width=15,
                    length=tk_prev_img_y, sliderlength=20)
tk_text_cropyb = Label(tk_cropy_frame, height=1, text="Crop bottom:")
tk_scale_yb = Scale(tk_cropy_frame, variable=new_img_yb,
                    resolution=1, borderwidth=1,
                    from_=tk_s_img_y-1, to=0, width=15,
                    length=tk_prev_img_y, sliderlength=20)

# Crop-X section
tk_cropx_frame = Frame(tk_content_frame)
tk_text_cropxl = Label(tk_cropx_frame, height=1,
                       text="Crop left:")
tk_scale_xl = Scale(tk_cropx_frame, variable=new_img_xl,
                    resolution=1, borderwidth=1, width=15,
                    from_=0, to=tk_s_img_x-1, orient=HORIZONTAL,
                    length=tk_prev_img_x, sliderlength=20)
tk_text_cropxr = Label(tk_cropx_frame, height=1,
                       text="Crop right:")
tk_scale_xr = Scale(tk_cropx_frame, variable=new_img_xr,
                    resolution=1, borderwidth=1, width=15,
                    from_=tk_s_img_x-1, to=0, orient=HORIZONTAL,
                    length=tk_prev_img_x, sliderlength=20)

# Button section
tk_button_frame = Frame(tk_cropy_frame)
tk_crop_button = Button(tk_button_frame, width=10, height=1,
                        text="Crop", bg="#6c6", fg="#060",
                        activebackground="#8d8", activeforeground="#060",
                        command=exec_crop)
tk_restore_button = Button(tk_button_frame, width=10, height=1,
                           text="Restore", command=exec_restore)
tk_close_button = Button(tk_button_frame, width=10, height=1,
                         text="Close", command=close_active)
# =================================TheEndOfObjects

# Display
# ================================================
tk_main_frame.pack(anchor="center")

# Crop-Y section(left)
tk_cropy_frame.grid(row=0, column=0, sticky='nw')
tk_text_cropyb.grid(row=0, column=0)
tk_text_cropyt.grid(row=0, column=1)
tk_scale_yb.grid(row=1, column=0)
tk_scale_yt.grid(row=1, column=1)
tk_text_r.grid(row=2, pady=(2, 0))

# The image(right)
tk_content_frame.grid(row=0, column=1, padx=(0, 15))
tk_text_image.grid(row=0)
tk_show_image.grid(row=1)

# Button section(left)
tk_button_frame.grid(row=2, columnspan=2, pady=(45, 0))
tk_crop_button.grid(row=2)
tk_restore_button.grid(row=3)
tk_close_button.grid(row=4)

# Crop-X section(right, bottom)
tk_cropx_frame.grid(row=3, pady=(0, 15))
tk_text_cropxl.grid(row=3, sticky='w')
tk_scale_xl.grid(row=4)
tk_text_cropxr.grid(row=5, sticky='e')
tk_scale_xr.grid(row=6)

root.mainloop()
# =================================TheEndOfDisplay
# =====================================TheEndOfGUI



# Save the image.
# ================================================
save_or_not = input("Save the image(y/n): ")
if save_or_not in ['y', 'Y']:
    file_name=input("Please input the file name: ")

    save_file(sharpened_img, file_name, file_extension, "")
    if tst_img != None: save_file(tst_img, file_name, file_extension, "_cropped")
else: print("\033[33mCanceled.\033[0m")
_exit(0)
# ================================================
