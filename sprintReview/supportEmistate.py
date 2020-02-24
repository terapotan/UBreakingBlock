if __name__ == '__main__':
    print("評価支援ツールVer1.0")
    while(1):
        earlyEndSchoolDay = input("学校が早めに終わる平日(5時前に終わる)で何日かかりそうですか?")
        lateEndSchoolDay = input("学校が遅く終わる平日(5時後に終わる)で何日かかりそうですか?")
        horidayDays = input("休日(完全off)で何日かかりそうですか?")

        print("評価ストーリポイントは{0}と推定されます。".format(3*int(earlyEndSchoolDay) + 5*int(lateEndSchoolDay) + 8*int(horidayDays)))
        continueCalc = input("もう一度実行しますか?(y/n)")

        if(continueCalc == "n"):
            break

        