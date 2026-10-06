"""
Professional Plotting Module for Academic Papers

This module provides utilities for creating publication-quality figures
for academic papers, including line plots, scatter plots, bar charts,
histograms, pie charts, heatmaps, and subplots.

Author: [Your Name]
Date: 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from typing import Tuple, List
import seaborn as sns

# Configure matplotlib for academic publications
plt.style.use('seaborn-v0_8-darkgrid')
rcParams['figure.dpi'] = 300
rcParams['savefig.dpi'] = 300
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.labelsize'] = 12
rcParams['axes.titlesize'] = 13
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10
rcParams['legend.fontsize'] = 10
rcParams['figure.titlesize'] = 14
rcParams['lines.linewidth'] = 1.5
rcParams['axes.linewidth'] = 0.8
rcParams['grid.linewidth'] = 0.5
rcParams['grid.alpha'] = 0.3
rcParams['axes.unicode_minus'] = False

# Support for Chinese characters (optional)
rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans', 'Arial']


def generate_trigonometric_data() -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Generate sample trigonometric data for demonstration.
    
    Returns:
        Tuple containing:
            - x: Domain values
            - y_sin: Sine function values
            - y_cos: Cosine function values
            - y_tan: Tangent function values (limited range)
    """
    x = np.linspace(0, 2 * np.pi, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x[:50])
    return x, y_sin, y_cos, y_tan


def plot_line_chart(x: np.ndarray, y_sin: np.ndarray, y_cos: np.ndarray,
                    output_path: str = 'line_chart.pdf') -> None:
    """
    Generate a publication-quality line plot.
    
    Args:
        x: X-axis data
        y_sin: Sine function data
        y_cos: Cosine function data
        output_path: Output file path (PDF recommended for papers)
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.plot(x, y_sin, label='sin(x)', linewidth=2.0, marker='o',
            markersize=3, alpha=0.8, color='#0173B2')
    ax.plot(x, y_cos, label='cos(x)', linewidth=2.0, marker='s',
            markersize=3, alpha=0.8, color='#DE8F05')
    
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.set_title('Comparison of Trigonometric Functions', fontsize=13, fontweight='bold')
    ax.legend(loc='best', frameon=True, shadow=True)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"✓ Line chart saved as '{output_path}'")
    plt.close()


def plot_scatter_chart(x: np.ndarray, y_sin: np.ndarray, y_cos: np.ndarray,
                       output_path: str = 'scatter_chart.pdf') -> None:
    """
    Generate a publication-quality scatter plot.
    
    Args:
        x: X-axis data
        y_sin: Sine function data
        y_cos: Cosine function data
        output_path: Output file path
    """
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.scatter(x, y_sin, alpha=0.6, s=30, label='sin(x)', 
               color='#0173B2', edgecolors='black', linewidth=0.5)
    ax.scatter(x, y_cos, alpha=0.6, s=30, label='cos(x)', 
               color='#DE8F05', edgecolors='black', linewidth=0.5)
    
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.set_title('Scatter Plot of Trigonometric Functions', fontsize=13, fontweight='bold')
    ax.legend(loc='best', frameon=True, shadow=True)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"✓ Scatter chart saved as '{output_path}'")
    plt.close()


def plot_bar_chart(output_path: str = 'bar_chart.pdf') -> None:
    """
    Generate a publication-quality bar chart.
    
    Args:
        output_path: Output file path
    """
    categories = ['Python', 'JavaScript', 'Java', 'C++', 'Go']
    values = np.array([95, 82, 78, 72, 88])
    colors = ['#0173B2', '#DE8F05', '#029E73', '#CC78BC', '#CA9161']
    
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(categories, values, color=colors, alpha=0.85,
                  edgecolor='black', linewidth=1.0)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height,
                f'{int(height)}', ha='center', va='bottom',
                fontsize=10, fontweight='bold')
    
    ax.set_ylabel('Score', fontsize=12)
    ax.set_ylim(0, 110)
    ax.set_title('Programming Language Popularity', fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(output_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"✓ Bar chart saved as '{output_path}'")
    plt.close()


def plot_histogram(output_path: str = 'histogram.pdf') -> None:
    """
    Generate a publication-quality histogram.
    
    Args:
        output_path: Output file path
    """
    data = np.random.randn(1000)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(data, bins=30, color='#0173B2', edgecolor='black',
            alpha=0.7, linewidth=0.8)
    
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Normal Distribution Histogram', fontsize=13, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(output_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"✓ Histogram saved as '{output_path}'")
    plt.close()


def plot_pie_chart(output_path: str = 'pie_chart.pdf') -> None:
    """
    Generate a publication-quality pie chart.
    
    Args:
        output_path: Output file path
    """
    labels = ['Frontend', 'Backend', 'DevOps', 'QA']
    sizes = [30, 35, 20, 15]
    colors = ['#0173B2', '#DE8F05', '#029E73', '#CC78BC']
    explode = (0.05, 0.05, 0, 0)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(sizes, explode=explode, labels=labels, colors=colors,
           autopct='%1.1f%%', shadow=True, startangle=90,
           textprops={'fontsize': 11})
    
    ax.set_title('Project Team Distribution', fontsize=13, fontweight='bold')
    ax.axis('equal')
    
    plt.tight_layout()
    plt.savefig(output_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"✓ Pie chart saved as '{output_path}'")
    plt.close()


def plot_heatmap(output_path: str = 'heatmap.pdf') -> None:
    """
    Generate a publication-quality heatmap.
    
    Args:
        output_path: Output file path
    """
    data = np.random.randn(10, 10)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(data, cmap='RdBu_r', aspect='auto', interpolation='nearest')
    
    cbar = plt.colorbar(im, ax=ax, label='Value', fraction=0.046, pad=0.04)
    cbar.ax.tick_params(labelsize=10)
    
    ax.set_xlabel('X Axis', fontsize=12)
    ax.set_ylabel('Y Axis', fontsize=12)
    ax.set_title('2D Heatmap', fontsize=13, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(output_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"✓ Heatmap saved as '{output_path}'")
    plt.close()


def plot_subplots(x: np.ndarray, y_sin: np.ndarray, y_cos: np.ndarray,
                   y_tan: np.ndarray, output_path: str = 'subplots.pdf') -> None:
    """
    Generate a publication-quality multi-panel figure.
    
    Args:
        x: X-axis data
        y_sin: Sine function data
        y_cos: Cosine function data
        y_tan: Tangent function data
        output_path: Output file path
    """
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    
    # Panel (a): Sine function
    axes[0, 0].plot(x, y_sin, 'b-', linewidth=2.0, label='sin(x)')
    axes[0, 0].set_title('(a) Sine Function', fontsize=12, fontweight='bold')
    axes[0, 0].set_ylabel('f(x)', fontsize=11)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend(loc='best')
    
    # Panel (b): Cosine function
    axes[0, 1].plot(x, y_cos, 'r-', linewidth=2.0, label='cos(x)')
    axes[0, 1].set_title('(b) Cosine Function', fontsize=12, fontweight='bold')
    axes[0, 1].set_ylabel('f(x)', fontsize=11)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend(loc='best')
    
    # Panel (c): Tangent function
    axes[1, 0].plot(x[:50], y_tan, 'g-', linewidth=2.0, label='tan(x)')
    axes[1, 0].set_title('(c) Tangent Function', fontsize=12, fontweight='bold')
    axes[1, 0].set_xlabel('x', fontsize=11)
    axes[1, 0].set_ylabel('f(x)', fontsize=11)
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend(loc='best')
    
    # Panel (d): Combined
    axes[1, 1].plot(x, y_sin, 'b-', label='sin(x)', linewidth=1.5, alpha=0.8)
    axes[1, 1].plot(x, y_cos, 'r-', label='cos(x)', linewidth=1.5, alpha=0.8)
    axes[1, 1].set_title('(d) Combined Functions', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('x', fontsize=11)
    axes[1, 1].set_ylabel('f(x)', fontsize=11)
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend(loc='best')
    
    plt.suptitle('Trigonometric Functions Analysis', fontsize=14, fontweight='bold', y=0.995)
    plt.tight_layout()
    plt.savefig(output_path, format='pdf', bbox_inches='tight', dpi=300)
    print(f"✓ Subplots saved as '{output_path}'")
    plt.close()


def main() -> None:
    """
    Main function: Generate all publication-quality figures.
    """
    print("=" * 60)
    print("Academic Publishing Quality Figure Generation")
    print("=" * 60)
    
    # Generate data
    print("\nGenerating data...")
    x, y_sin, y_cos, y_tan = generate_trigonometric_data()
    print("✓ Data generation complete")
    
    # Generate all figures
    print("\nGenerating figures...\n")
    
    plot_line_chart(x, y_sin, y_cos)
    plot_scatter_chart(x, y_sin, y_cos)
    plot_bar_chart()
    plot_histogram()
    plot_pie_chart()
    plot_heatmap()
    plot_subplots(x, y_sin, y_cos, y_tan)
    
    print("\n" + "=" * 60)
    print("✓ All figures generated successfully!")
    print("  Output format: PDF (recommended for academic papers)")
    print("=" * 60)


if __name__ == '__main__':
    main()
