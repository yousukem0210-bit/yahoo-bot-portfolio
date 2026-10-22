
def score_pc(pc):
    """中古PCを簡易的に100点満点で評価するサンプル。"""
    score = 0

    # CPU: 最大40点
    score += min(max(pc["cpu_generation"] - 7, 0) * 8, 40)

    # メモリ: 最大20点
    if pc["memory_gb"] >= 16:
        score += 20

    # SSD: 最大10点
    if pc["ssd_gb"] >= 256:
        score += 10

    # ディスプレイ: 最大10点
    if pc["screen_inches"] >= 13 and pc["full_hd"]:
        score += 10

    # 価格: 最大10点
    if pc["price_yen"] <= 30000:
        score += 10

    # 商品状態: 最大10点
    if pc["working"]:
        score += 10

    return score


if __name__ == "__main__":
    sample = {
        "cpu_generation": 11,
        "memory_gb": 16,
        "ssd_gb": 256,
        "screen_inches": 14,
        "full_hd": True,
        "price_yen": 25000,
        "working": True,
    }

    print(f"評価スコア: {score_pc(sample)} / 100")
