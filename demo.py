import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体支持
rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
rcParams['axes.unicode_minus'] = False

# 1. 生成示例数据
def generate_data():
    """生成用于绘图的示例数据"""
    x = np.linspace(0, 2*np.pi, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x[:50])  # 限制范围避免无穷大
    return x, y_sin, y_cos, y_tan

# 2. 绘制线性图
def plot_line_chart(x, y_sin, y_cos):
    """绘制线性图"""
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_sin, label='sin(x)', linewidth=2, marker='o', markersize=4)
    plt.plot(x, y_cos, label='cos(x)', linewidth=2, marker='s', markersize=4)
    plt.title('三角函数对比', fontsize=14, fontweight='bold')
    plt.xlabel('X 轴', fontsize=12)
    plt.ylabel('Y 轴', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('line_chart.png', dpi=300, bbox_inches='tight')
    print("✓ 线性图已保存为 'line_chart.png'")
    plt.show()

# 3. 绘制散点图
def plot_scatter(x, y_sin, y_cos):
    """绘制散点图"""
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y_sin, alpha=0.6, s=50, label='sin(x)', color='red')
    plt.scatter(x, y_cos, alpha=0.6, s=50, label='cos(x)', color='blue')
    plt.title('三角函数散点图', fontsize=14, fontweight='bold')
    plt.xlabel('X 轴', fontsize=12)
    plt.ylabel('Y 轴', fontsize=12)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('scatter_chart.png', dpi=300, bbox_inches='tight')
    print("✓ 散点图已保存为 'scatter_chart.png'")
    plt.show()

# 4. 绘制柱状图
def plot_bar_chart():
    """绘制柱状图"""
    categories = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
    values = np.array([95, 82, 78, 72, 88])
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)
    
    # 在柱子上添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.title('编程语言受欢迎程度', fontsize=14, fontweight='bold')
    plt.ylabel('评分', fontsize=12)
    plt.ylim(0, 110)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig('bar_chart.png', dpi=300, bbox_inches='tight')
    print("✓ 柱状图已保存为 'bar_chart.png'")
    plt.show()

# 5. 绘制直方图
def plot_histogram():
    """绘制直方图"""
    data = np.random.randn(1000)  # 生成1000个正态分布数据
    
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title('正态分布直方图', fontsize=14, fontweight='bold')
    plt.xlabel('数值', fontsize=12)
    plt.ylabel('频率', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig('histogram.png', dpi=300, bbox_inches='tight')
    print("✓ 直方图已保存为 'histogram.png'")
    plt.show()

# 6. 绘制饼图
def plot_pie_chart():
    """绘制饼图"""
    labels = ['Frontend', 'Backend', 'DevOps', 'QA']
    sizes = [30, 35, 20, 15]
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    explode = (0.05, 0.05, 0, 0)  # 突出显示前两个切片
    
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 12})
    plt.title('项目团队分布', fontsize=14, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('pie_chart.png', dpi=300, bbox_inches='tight')
    print("✓ 饼图已保存为 'pie_chart.png'")
    plt.show()

# 7. 绘制热力图
def plot_heatmap():
    """绘制热力图"""
    data = np.random.randn(10, 10)
    
    plt.figure(figsize=(10, 8))
    im = plt.imshow(data, cmap='coolwarm', aspect='auto', interpolation='nearest')
    plt.colorbar(im, label='数值')
    plt.title('2D 热力图', fontsize=14, fontweight='bold')
    plt.xlabel('X 轴', fontsize=12)
    plt.ylabel('Y 轴', fontsize=12)
    plt.tight_layout()
    plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
    print("✓ 热力图已保存为 'heatmap.png'")
    plt.show()

# 8. 绘制多子图
def plot_subplots(x, y_sin, y_cos, y_tan):
    """绘制多个子图"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # 子图1: 正弦波
    axes[0, 0].plot(x, y_sin, 'b-', linewidth=2, label='sin(x)')
    axes[0, 0].set_title('正弦函数', fontsize=12, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    
    # 子图2: 余弦波
    axes[0, 1].plot(x, y_cos, 'r-', linewidth=2, label='cos(x)')
    axes[0, 1].set_title('余弦函数', fontsize=12, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()
    
    # 子图3: 正切波
    axes[1, 0].plot(x[:50], y_tan, 'g-', linewidth=2, label='tan(x)')
    axes[1, 0].set_title('正切函数', fontsize=12, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    
    # 子图4: 组合图
    axes[1, 1].plot(x, y_sin, 'b-', label='sin(x)', linewidth=1.5)
    axes[1, 1].plot(x, y_cos, 'r-', label='cos(x)', linewidth=1.5)
    axes[1, 1].set_title('三角函数组合', fontsize=12, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()
    
    plt.suptitle('多子图绘制示例', fontsize=16, fontweight='bold', y=1.00)
    plt.tight_layout()
    plt.savefig('subplots.png', dpi=300, bbox_inches='tight')
    print("✓ 多子图已保存为 'subplots.png'")
    plt.show()

# 主程序
def main():
    """主函数 - 执行所有绘图操作"""
    print("=" * 50)
    print("欢迎使用完整绘图程序！")
    print("=" * 50)
    
    # 生成数据
    print("\n正在生成数据...")
    x, y_sin, y_cos, y_tan = generate_data()
    print("✓ 数据生成完成")
    
    # 执行各种绘图
    print("\n开始绘制图表...\n")
    
    plot_line_chart(x, y_sin, y_cos)
    plot_scatter(x, y_sin, y_cos)
    plot_bar_chart()
    plot_histogram()
    plot_pie_chart()
    plot_heatmap()
    plot_subplots(x, y_sin, y_cos, y_tan)
    
    print("\n" + "=" * 50)
    print("✓ 所有图表已生成完毕！")
    print("=" * 50)

if __name__ == '__main__':
    main()
