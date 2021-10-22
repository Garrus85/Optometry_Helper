

def header():
    print("----------------------------------")
    print("---- OPTOMETRY HELPER PROGRAM ----")
    print("----------------------------------")


def menu():
    print("Please choose what service you require")
    print("""
       [1] - Transpose Rx
       [2] - BVD Calculator
       [3] - Glaucoma SIGN Guideline Referral
           """)
    return input()

def transpose(re_rx, le_rx):
    re_rx_split = split_rx(re_rx)
    transposed_re_rx = f'R:{transpose_helper(re_rx_split)}'

    le_rx_split = split_rx(le_rx)
    transposed_le_rx = f'L:{transpose_helper(le_rx_split)}'

    return [transposed_re_rx, transposed_le_rx]


def split_rx(rx):

    rx_list = rx.split("/")
    sph = rx_list[0]
    cyl_and_axis = rx_list[1]
    cylaxis = cyl_and_axis.split("x")
    cyl = cylaxis[0]
    axis = cylaxis[1]
    return [sph, cyl, axis]


def transpose_helper(rx_list):
    sph = float(rx_list[0])
    cyl = float(rx_list[1])
    axis = int(rx_list[2])
    new_sphere = format((sph + cyl), '.2f')
    if float(new_sphere) > 0:
        new_sphere = "+"+ str(new_sphere)
    new_cyl = format(-(cyl), '.2f')
    new_axis = axis + 90 if axis < 90 else axis - 90
    if float(new_cyl) > 0:
        return f'{new_sphere}/+{new_cyl}x{new_axis}'
    else:
        return f'{new_sphere}/{new_cyl}x{new_axis}'



def back_vertex_distance(rx, old_bvd, new_bvd):

    if len(rx) > 5:
        rx_split = split(rx)
        f = float(rx_split[0])
    else:
        f = float(rx)
    bvd_change = (int(old_bvd) - int(new_bvd)) / 1000
    k = format(f / (1-(bvd_change * f)), '.2f')
    return f'\nThe new spherical power is {k}D'


def glaucoma_referral_info():

    iop = input("Enter the patients intraocular pressure? ")
    cct = input("What is the central corneal thickness? ")
    vh = input("What is the angle grade [0 = closed, 4 = open] ")
    vf = input("Is there a repeatable visual field defect? [Y/N] ")
    disc = input("Is there glaucomatous disc changes? [Y/N] ")
    age = input("What is the patients age? ")
    glaucoma_referral(iop, cct, vh, vf, disc, age)


def glaucoma_referral(iop, cct, vh, vf, disc, age):

    iop = int(iop)
    cct = int(cct)
    age = int(age)
    vh = int(vh)
    disc = disc.upper()
    vf = vf.upper()

    if vf == "Y":
        print("\nReferral to secondary eye care is indicated.")
    elif disc == "Y":
        print("\nReferral to secondary eye care is indicated.")
    else:
        if iop >= 40:
            print("\nImmediate referral required as IOP >= 40mmg.")
        elif iop >= 30:
            print("\nUrgent referral required as IOP >= 30mmhg.")
        elif iop >= 26:
            print("\nRoutine referral is required as IOP >= 26mmhg.")
        elif 21 < iop <= 25:
            if cct > 555:
                print("""\nNo need to refer at this stage. Referral is indicated if IOP > 26mmhg without glaucomatous "
                           optic nerve changes or a repeatable visual field defect.""")
            elif age < 66 and cct < 555:
                print("\nConsider referral to secondary eye care.")
            else:
                print("\nPatient may be monitored in the community.")
        elif vh in {0, 1}:
            print("\nConsider referral due to risk of angle closure.")
        else:
            print("\nPatient can be monitored in community.")
    print("----------------------------------")
    print("\n")

