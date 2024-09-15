import json
import pathlib

# 定义目录
ROOT_DIR = pathlib.Path(__file__).parent.parent
BOOKSOURCE_ROOT_DIR = ROOT_DIR / "BookSource"
DOCS_DIR = ROOT_DIR.parent / "docs"
WEBSITES_MD_PATH = DOCS_DIR / "websites.md"

# 配置文件夹分组别名
FOLDER_ALIASES = {
    "China_based_bookSource": "国轻小说",
    "Japan_based_bookSource": "日轻小说",
    "Japanese_original_bookSource": "日语原版轻小说"
}

def json_list(kind_path):
    """获取指定路径下所有JSON文件的路径列表，排除archive文件夹"""
    json_files = []
    for path in pathlib.Path(kind_path).rglob("*.json"):
        if 'archive' not in path.parts:
            json_files.append(path)
    return json_files

def extract_website_info(source_dir):
    """从JSON文件中提取网站信息"""
    website_info = []
    json_files = json_list(source_dir)
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                name = item.get("bookSourceName", "unknown")
                url = item.get("bookSourceUrl", "unknown")
                website_info.append((name, url))
    return website_info

def generate_markdown():
    """生成支持网站的Markdown文件"""
    markdown_content = "# 支持网站列表\n> [!CAUTION]\n>此文档由脚本自动生成，可能存在错误，请以实际书源为准。\n\n"
    for folder, alias in FOLDER_ALIASES.items():
        source_dir = BOOKSOURCE_ROOT_DIR / folder
        website_info = extract_website_info(source_dir)
        markdown_content += f"## {alias}\n"
        markdown_content += "| 名称 | 网址 |\n"
        markdown_content += "| :--: | :--: |\n"
        for name, url in website_info:
            markdown_content += f"| {name} | {url} |\n"
        markdown_content += "\n"

    # 检查文件是否存在，如果不存在则创建
    if not DOCS_DIR.exists():
        DOCS_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Directory {DOCS_DIR} does not exist. Creating new directory...")

    with open(WEBSITES_MD_PATH, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"Markdown file generated at {WEBSITES_MD_PATH}")

if __name__ == "__main__":
    generate_markdown()