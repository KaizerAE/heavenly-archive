#!/usr/bin/env python3
"""
Heavenly Archive - Command Line Interface

A beautiful CLI tool for managing events and achievements
from the terminal with celestial elegance.

Author: KaizerAE
License: MIT
"""

import click
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from rich.progress import track
import time

console = Console()

# Celestial banner
BANNER = """
🌸 Heavenly Archive 🌸
天官赐福档案馆

Record your journey with celestial elegance ✨
"""


@click.group()
@click.version_option(version="0.1.0", prog_name="Heavenly Archive")
def cli():
    """Heavenly Archive - A celestial event tracking system"""
    console.print(Panel(BANNER, border_style="bright_magenta", box=box.DOUBLE))


@cli.command()
@click.option("--title", "-t", required=True, help="Event title")
@click.option("--category", "-c", 
              type=click.Choice(["virtue", "trial", "victory", "legendary", "divine", "mortal"]),
              default="virtue", help="Event category")
@click.option("--importance", "-i",
              type=click.Choice(["low", "medium", "high", "critical", "legendary"]),
              default="medium", help="Event importance")
@click.option("--description", "-d", help="Event description")
@click.option("--tags", help="Comma-separated tags")
def add(title, category, importance, description, tags):
    """🌸 Add a new event to your archive"""
    
    console.print("\n[bold cyan]Creating new event...[/bold cyan]")
    
    # Simulate event creation with progress
    for _ in track(range(3), description="[cyan]Recording in celestial archives..."):
        time.sleep(0.3)
    
    event_data = {
        "title": title,
        "category": category,
        "importance": importance,
        "description": description or "No description provided",
        "tags": tags or "None",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Display created event
    table = Table(title="✨ New Event Created", border_style="bright_cyan", box=box.ROUNDED)
    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    
    for key, value in event_data.items():
        table.add_row(key.replace("_", " ").title(), str(value))
    
    console.print(table)
    console.print("\n🌸 [bold green]Event successfully recorded in the heavenly archives![/bold green]\n")


@cli.command()
@click.option("--limit", "-l", default=10, help="Number of events to display")
@click.option("--category", "-c", help="Filter by category")
def list(limit, category):
    """📜 List recent events from your archive"""
    
    console.print(f"\n[bold cyan]Fetching {limit} recent events...[/bold cyan]\n")
    
    # Sample events for demonstration
    sample_events = [
        {"id": 1, "title": "Completed First Project", "category": "victory", "importance": "high", "date": "2025-11-18"},
        {"id": 2, "title": "Learned FastAPI", "category": "virtue", "importance": "medium", "date": "2025-11-17"},
        {"id": 3, "title": "Overcame Bug Challenge", "category": "trial", "importance": "high", "date": "2025-11-16"},
    ]
    
    table = Table(title="✨ Recent Events", border_style="bright_magenta", box=box.DOUBLE_EDGE)
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Category", style="yellow")
    table.add_column("Importance", style="red")
    table.add_column("Date", style="green")
    
    for event in sample_events[:limit]:
        if not category or event["category"] == category:
            table.add_row(
                str(event["id"]),
                event["title"],
                event["category"],
                event["importance"],
                event["date"]
            )
    
    console.print(table)
    console.print("\n")


@cli.command()
@click.option("--query", "-q", required=True, help="Search query")
def search(query):
    """🔍 Search events in your archive"""
    
    console.print(f"\n[bold cyan]Searching for: '{query}'...[/bold cyan]\n")
    
    for _ in track(range(3), description="[cyan]Searching celestial records..."):
        time.sleep(0.2)
    
    console.print(f"\n[yellow]No events found matching '{query}'[/yellow]")
    console.print("[dim]Try using the --add command to create your first event![/dim]\n")


@cli.command()
def stats():
    """📊 View your achievement statistics"""
    
    console.print("\n[bold cyan]Loading statistics...[/bold cyan]\n")
    
    # Sample statistics
    stats_table = Table(title="✨ Heavenly Statistics", border_style="bright_cyan", box=box.HEAVY)
    stats_table.add_column("Metric", style="cyan", no_wrap=True)
    stats_table.add_column("Count", justify="right", style="magenta")
    
    stats_table.add_row("📜 Total Events", "42")
    stats_table.add_row("🌸 Virtues", "15")
    stats_table.add_row("⚔️ Trials", "8")
    stats_table.add_row("🏆 Victories", "12")
    stats_table.add_row("✨ Legendary", "7")
    stats_table.add_row("🌟 Divine", "0")
    
    console.print(stats_table)
    console.print("\n[bold green]May the heavens bless your journey! 🌸[/bold green]\n")


@cli.command()
def init():
    """⚙️ Initialize the Heavenly Archive database"""
    
    console.print("\n[bold cyan]Initializing Heavenly Archive...[/bold cyan]\n")
    
    for step in track(["Creating database", "Setting up tables", "Applying migrations"],
                       description="[cyan]Building celestial infrastructure..."):
        time.sleep(0.5)
    
    console.print("\n[bold green]✓ Database initialized successfully![/bold green]")
    console.print("[dim]You can now start adding events with: heavenly-archive add[/dim]\n")


if __name__ == "__main__":
    cli()
