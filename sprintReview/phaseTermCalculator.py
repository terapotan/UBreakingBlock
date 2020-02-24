# coding: utf-8
import sys
periodSpentInProject = input("プロジェクトにかけるSprint数を入力して下さい>")
periodSpentInProject = int(periodSpentInProject)
if (periodSpentInProject > 24):
    print("プロジェクトにかけられるスプリント数は最大24Sprintsまでです。")
    sys.exit()

alphaPeriod = periodSpentInProject * (6/11)
debugPeriod = alphaPeriod / 2
soundEffectCreatingPeriod = periodSpentInProject - (alphaPeriod + debugPeriod)

print("本開発期間(prealphaリリース～alpha版リリース):{0}".format(alphaPeriod))
print("画像・効果音等作成期間(alpha版リリース～beta版リリース){0}".format(soundEffectCreatingPeriod))
print("デバッグ期間:{0}".format(debugPeriod))

input("")