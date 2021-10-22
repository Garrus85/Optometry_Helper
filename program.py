import services

def main():

    choice = services.menu()

    if choice == "1":
        re = input("Please enter the Right eye prescription: ")
        le = input("Please enter the Left eye prescription: ")
        print(services.transpose(re, le))
    elif choice == "2":
        rx = input("What is the spherical power [D]? ")
        tested_bvd = input("What was the original back vertex distance [mm]? ")
        new_bvd = input("What os the new back vertex distance [0 for contact lenses]? ")
        print(services.back_vertex_distance(rx, tested_bvd, new_bvd))
    elif choice == "3":
        services.glaucoma_referral_info()
    else:
        print("Invalid input.")

    main()


if __name__ == "__main__":
    services.header()
    main()
