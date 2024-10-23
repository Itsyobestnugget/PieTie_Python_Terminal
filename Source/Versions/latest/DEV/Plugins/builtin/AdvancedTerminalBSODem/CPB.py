# Error codes
err = "NOERR_"
err_desc = "Test/base error. also fallback. Unkown"
err1 = "AAAAA1"
err1_desc = "KEEPUP. Version not up to date."
err2 = "AAAAA2"
err2_desc = ""
err3 = "AAAAA3"
err3_desc = ""
err4 = "AAAAA4"
err4_desc = ""
err5 = "AAAAA5"
err5_desc = ""
err6 = "AAAAA6"
err6_desc = ""
err7 = "AAAAA7"
err7_desc = ""
err8 = "AAAAA8"
err8_desc = ""
err9 = "AAAAA9"
err9_desc = ""
err10 = "AAAAB0"
err10_desc = ""
fallbackerr = err
fallbackerr_desc = err_desc
# Error codes end

def CBP(reason, user):
        BSODerror = reason
        print("\n \nCALLBACKPING")
        print("  ,-.       _,---._ __  / \ \n /  )    .-'       `./ /   \ \n(  (   ,'            `/    /|                         \n  `.              ,  \ \ /  | \n   /`.          ,'-`----Y   | \n  (            ;        |   ' \n  |  ,-.    ,-'         |  / \n  |  | (   |    oops... | / \n  )  |  \  `.___________|/ \n  `--'   `--') \n \n Apparently, the terminal ran into a problem... thats not good\n this would be where we would collect data. its being written to a log file, see reason for crash below \n \n")
        print("🠇🠇🠇 Reason 🠇🠇🠇\n")
        print(BSODerror)
        print("\n🠅🠅🠅 Reason 🠅🠅🠅")
        log.write("CALLBACKPING(bsod) initiated by " + user + " for " + reason)
        exit()