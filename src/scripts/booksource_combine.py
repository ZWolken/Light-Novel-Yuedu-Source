import json
import pathlib
from datetime import datetime

# 定义书源根目录
BOOKSOURCE_ROOT_DIR = pathlib.Path(__file__).parent.parent / "BookSource"
ROOT_DIR = pathlib.Path(__file__).parent.parent

# 配置文件夹分组别名
FOLDER_ALIASES = {
    "China_based_bookSource": "国轻小说",
    "Japan_based_bookSource": "日轻小说",
    "Japanese_original_bookSource": "日本語Web小説"
}

def json_list(kind_path):
    """获取指定路径下所有JSON文件的路径列表"""
    return list(pathlib.Path(kind_path).rglob("*.json"))


def combine_json_files(source_dir, group_name):
    """将指定目录下的所有JSON文件整合成一个JSON文件，并添加分组"""
    combined_data = []
    json_files = json_list(source_dir)

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                if "bookSourceGroup" in item and item["bookSourceGroup"]:
                    item["bookSourceGroup"] += f",{group_name}"
                else:
                    item["bookSourceGroup"] = group_name
            combined_data.extend(data)

    return combined_data


def save_combined_json(data, output_path):
    """将整合后的JSON数据保存到指定路径"""
    output_path.parent.mkdir(parents=True, exist_ok=True)  # 创建文件夹
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    """主函数"""
    # 获取当前日期
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 遍历书源根目录下的每个子目录，排除 archive 文件夹
    for source_dir in BOOKSOURCE_ROOT_DIR.iterdir():
        if source_dir.is_dir() and source_dir.name != "archive":
            # 获取文件夹别名，如果没有配置别名则使用文件夹名称
            alias = FOLDER_ALIASES.get(source_dir.name, source_dir.name)
            group_name = f"{alias}({current_date})\nGitHub@ZWolken"
            combined_data = combine_json_files(source_dir, group_name)
            output_path = ROOT_DIR / "build" / f"{source_dir.name}.json"
            save_combined_json(combined_data, output_path)
            print(f"Combined JSON saved to {output_path}")


if __name__ == "__main__":
    main()
