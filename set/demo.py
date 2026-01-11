"""
Set 範例：區域巡檢狀態管理

情境：
在工安監控系統中，需要追蹤哪些區域已經巡檢、哪些還沒。
使用 Set 可以快速找出「尚未巡檢的區域」。

執行方式：
python demo.py
"""


def main():
    print("=== Set 範例：區域巡檢狀態管理 ===\n")

    # === 1. Set 基本特性：不重複 ===

    print("1. Set 的不重複特性")
    print("-" * 40)

    # 今日違規記錄（同一人可能多次違規）
    violations_today = [
        "王小明", "李大華", "王小明", "張三", "李大華", "王小明"
    ]
    print(f"原始違規記錄: {violations_today}")
    print(f"記錄筆數: {len(violations_today)}")

    # 轉成 Set 自動去重
    violators = set(violations_today)
    print(f"違規人員（去重）: {violators}")
    print(f"實際違規人數: {len(violators)}")

    # === 2. 差集：找出尚未完成的項目 ===

    print("\n2. 差集運算：找出尚未巡檢的區域")
    print("-" * 40)

    # 所有需要巡檢的區域
    all_zones = {"大門入口", "施工區A", "施工區B", "倉庫", "辦公室", "停車場"}

    # 今日已巡檢的區域
    inspected_zones = {"大門入口", "施工區A", "倉庫"}

    # 差集：找出尚未巡檢的區域
    pending_zones = all_zones - inspected_zones

    print(f"所有區域: {all_zones}")
    print(f"已巡檢: {inspected_zones}")
    print(f"尚未巡檢: {pending_zones}")

    # === 3. 交集：找出同時符合條件的項目 ===

    print("\n3. 交集運算：找出高風險人員")
    print("-" * 40)

    # 今日違規人員
    violators = {"王小明", "李大華", "張三", "陳小美"}

    # 歷史黑名單（累犯）
    blacklist = {"王小明", "趙六", "張三"}

    # 交集：違規 + 黑名單 = 高風險人員
    high_risk = violators & blacklist

    print(f"今日違規人員: {violators}")
    print(f"歷史黑名單: {blacklist}")
    print(f"高風險人員（違規+黑名單）: {high_risk}")

    # === 4. 聯集：合併所有項目 ===

    print("\n4. 聯集運算：合併通知名單")
    print("-" * 40)

    # 需要通知的主管
    managers = {"主管A", "主管B"}

    # 需要通知的安全員
    safety_officers = {"安全員1", "安全員2", "主管A"}  # 主管A 也是安全員

    # 聯集：合併所有需要通知的人
    notify_list = managers | safety_officers

    print(f"主管: {managers}")
    print(f"安全員: {safety_officers}")
    print(f"通知名單（自動去重）: {notify_list}")

    # === 5. 對稱差集：找出「只在其中一邊」的項目 ===

    print("\n5. 對稱差集：找出差異")
    print("-" * 40)

    # 昨日違規人員
    yesterday = {"王小明", "李大華", "張三"}

    # 今日違規人員
    today = {"李大華", "陳小美", "趙六"}

    # 對稱差集：只在昨天 或 只在今天（不在兩者同時出現）
    diff = yesterday ^ today

    print(f"昨日違規: {yesterday}")
    print(f"今日違規: {today}")
    print(f"差異（新增或消失）: {diff}")

    # === 6. 實務應用：巡檢進度追蹤 ===

    print("\n6. 實務應用：巡檢進度追蹤")
    print("-" * 40)

    all_zones = {"A區", "B區", "C區", "D區", "E區"}
    inspected = set()

    # 模擬巡檢過程
    inspection_log = ["A區", "B區", "A區", "C區"]  # A區 重複巡檢

    for zone in inspection_log:
        inspected.add(zone)
        pending = all_zones - inspected
        progress = len(inspected) / len(all_zones) * 100
        print(f"完成 {zone} → 進度: {progress:.0f}% | 剩餘: {pending}")

    print("\n=== 完成 ===")


if __name__ == "__main__":
    main()
