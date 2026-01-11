"""
Tuple 範例：攝影機配置管理

情境：
在工安監控系統中，每台攝影機有固定的配置（ID、位置、IP）。
這些配置不應該被意外修改，因此使用 Tuple 來儲存。

執行方式：
python demo.py
"""


def main():
    print("=== Tuple 範例：攝影機配置管理 ===\n")

    # === 1. 建立攝影機配置（使用 Tuple） ===

    print("1. 建立攝影機配置")
    print("-" * 40)

    camera_1 = ("CAM-001", "大門入口", "192.168.1.101")
    camera_2 = ("CAM-002", "施工區A", "192.168.1.102")
    camera_3 = ("CAM-003", "倉庫門口", "192.168.1.103")

    print(f"攝影機 1: {camera_1}")
    print(f"攝影機 2: {camera_2}")
    print(f"攝影機 3: {camera_3}")

    # === 2. 存取 Tuple 元素 ===

    print("\n2. 存取 Tuple 元素")
    print("-" * 40)

    print(f"攝影機 ID: {camera_1[0]}")
    print(f"位置: {camera_1[1]}")
    print(f"IP: {camera_1[2]}")

    # === 3. Tuple 不可修改 ===

    print("\n3. 嘗試修改 Tuple（會報錯）")
    print("-" * 40)

    try:
        camera_1[1] = "後門"  # TypeError!
    except TypeError as e:
        print(f"錯誤：{e}")
        print("→ Tuple 不可修改，這是預期的行為")

    # === 4. 如果需要「更新」，建立新的 Tuple ===

    print("\n4. 透過建立新 Tuple 來「更新」")
    print("-" * 40)

    print(f"原配置: {camera_1}")

    # 建立新的 Tuple，保留不變的部分，修改需要更新的部分
    camera_1_updated = (camera_1[0], "後門出口", camera_1[2])

    print(f"新配置: {camera_1_updated}")

    # === 5. Tuple vs List 比較 ===

    print("\n5. Tuple vs List 比較")
    print("-" * 40)

    # Tuple：不可變
    config_tuple = ("CAM-001", "大門入口", "192.168.1.101")

    # List：可變
    config_list = ["CAM-001", "大門入口", "192.168.1.101"]
    config_list[1] = "後門"  # List 可以直接修改

    print(f"Tuple（不可變）: {config_tuple}")
    print(f"List（已修改）: {config_list}")

    # === 6. 實務應用：違規記錄 ===

    print("\n6. 實務應用：違規記錄")
    print("-" * 40)

    # 違規記錄使用 Tuple，確保不可竄改
    violation_1 = ("2024-01-15 10:30", "施工區A", "未戴安全帽", "high")
    violation_2 = ("2024-01-15 11:45", "倉庫門口", "未穿反光背心", "medium")

    # 多筆記錄存入 List
    violations = [violation_1, violation_2]

    print("違規記錄清單：")
    for i, v in enumerate(violations, 1):
        print(f"  {i}. 時間={v[0]}, 地點={v[1]}, 類型={v[2]}, 嚴重={v[3]}")

    print("\n=== 完成 ===")


if __name__ == "__main__":
    main()
