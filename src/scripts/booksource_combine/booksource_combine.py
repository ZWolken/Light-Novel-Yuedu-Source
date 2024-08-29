import json
import pathlib

# 定义书源根目录
BOOKSOURCE_ROOT_DIR = pathlib.Path(__file__).parent.parent.parent / "BookSource"


def json_list(kind_path):
    """获取指定路径下所有JSON文件的路径列表"""
    return list(pathlib.Path(kind_path).rglob("*.json"))


def combine_json_files(source_dir):
    """将指定目录下的所有JSON文件整合成一个JSON文件"""
    combined_data = []
    json_files = json_list(source_dir)

    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            combined_data.extend(data)

    return combined_data


def save_combined_json(data, output_path):
    """将整合后的JSON数据保存到指定路径"""
    output_path.parent.mkdir(parents=True, exist_ok=True)  # 创建文件夹
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def main():
    # 遍历书源根目录下的每个子目录
    for source_dir in BOOKSOURCE_ROOT_DIR.iterdir():
        if source_dir.is_dir():
            combined_data = combine_json_files(source_dir)
            output_path = BOOKSOURCE_ROOT_DIR / "build" / f"{source_dir.name}.json"
            save_combined_json(combined_data, output_path)
            print(f"Combined JSON saved to {output_path}")


if __name__ == "__main__":
    main()