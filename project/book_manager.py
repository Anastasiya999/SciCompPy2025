import pandas as pd
import os
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

FILE_NAME = 'books_db.csv'

def load_books_from_csv(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ Error reading CSV file: {e}")
        return pd.DataFrame()
    expected_columns = {"Title", "Author", "Year", "Genre"}
    missing = expected_columns - set(df.columns)
    if missing:
        print(f"⚠️ Missing expected columns in CSV: {missing}")
        return pd.DataFrame()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return df

def load_database():
    global FILE_NAME

    print("📚 Book Database Initialization")
    while True:
        choice = input("Do you want to (L)oad an existing database or (C)reate a new one? [L/C]: ").strip().lower()
        if choice == 'l':
            path = input("Enter path to CSV file: ").strip()
            df = load_books_from_csv(path)
            if not df.empty:
                print(f"✅ Loaded database with {len(df)} records.")
                FILE_NAME = path
                return df
            else:
                print("❌ Failed to load database. Try again.")
        elif choice == 'c':
            while True:
                filename = input("Enter new filename to save database (e.g. my_books.csv): ").strip()
                if not filename:
                    print("❌ Filename cannot be empty.")
                    continue
                if os.path.exists(filename):
                    print(f"❌ File '{filename}' already exists. Please choose a different name.")
                else:
                    FILE_NAME = filename
                    print(f"🆕 Creating a new empty database with filename '{FILE_NAME}'.")
                    df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])
                    return df
        else:
            print("❌ Invalid choice. Please enter 'L' or 'C'.")

def save_database(df):
    df.to_csv(FILE_NAME, index=False)

def list_books(df):
    if df.empty:
        print("No books in the database.")
    else:
        print("\nBook List:")
        print(df.to_string(index=False))

def insert_book(df):
    while True:
        title = input("Enter book title: ").strip()
        if title:
            break
        print("❌ Title cannot be empty.")

    while True:
        author = input("Enter author: ").strip()
        if author:
            break
        print("❌ Author cannot be empty.")

    year = input("Enter publication year: ").strip()
    genre = input("Enter genre: ").strip()

    new_book = pd.DataFrame([{
        'Title': title,
        'Author': author,
        'Year': year,
        'Genre': genre
    }])
    df = pd.concat([df, new_book], ignore_index=True)
    save_database(df)
    print(f"✅ Book '{title}' added.")
    return df


def remove_book(df):
    if df.empty:
        print("📭 No books to remove.")
        return df

    print("\n📑 Remove Book")
    print("1. Remove by title")
    print("2. Don't remember exact title. List books")
    choice = input("Choose removal method (1 or 2): ").strip()

    if choice == '1':
        title = input("Enter the title of the book to remove: ").strip()
        matches = df[df['Title'].str.lower() == title.lower()]
        if not matches.empty:
            print(f"\n⚠️ Found {len(matches)} matching book(s):")
            print(matches[['Title', 'Author', 'Year', 'Genre']].to_string(index=False))
            confirm = input("Are you sure you want to delete this book? (y/n): ").strip().lower()
            if confirm == 'y':
                df = df[df['Title'].str.lower() != title.lower()]
                save_database(df)
                print(f"🗑️ Book '{title}' removed.")
            else:
                print("❎ Deletion canceled.")
        else:
            print("❌ Book not found.")

    elif choice == '2':
        print("\n📋 Book Index List:")
        print(df[['Title']].reset_index())

        try:
            index = int(input("Enter the index of the book to remove: ").strip())
            if 0 <= index < len(df):
                book = df.iloc[index]
                print(f"\n⚠️ You selected: {book['Title']} by {book['Author']} ({book['Year']}, {book['Genre']})")
                confirm = input("Are you sure you want to delete this book? (y/n): ").strip().lower()
                if confirm == 'y':
                    df = df.drop(index).reset_index(drop=True)
                    save_database(df)
                    print(f"🗑️ Book '{book['Title']}' removed by index.")
                else:
                    print("❎ Deletion canceled.")
            else:
                print("❌ Invalid index.")
        except ValueError:
            print("❌ Please enter a valid integer index.")
    else:
        print("❗ Invalid option.")

    return df


def search_books(df):
    keyword = input("Enter search keyword (title or author): ")
    results = df[df['Title'].str.contains(keyword, case=False, na=False) |
                 df['Author'].str.contains(keyword, case=False, na=False)]
    if results.empty:
        print("🔍 No matching books found.")
    else:
        print("\n🔎 Search Results:")
        print(results.to_string(index=False))

def main():
    db = load_database()
    while True:
        print("\n📘 Book Database Menu")
        print("1. List books")
        print("2. Add book")
        print("3. Remove book")
        print("4. Search books")
        print("5. Show genre graph")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            list_books(db)
        elif choice == '2':
            db = insert_book(db)
        elif choice == '3':
            db = remove_book(db)
        elif choice == '4':
            search_books(db)
        elif choice == '5':
            show_genre_graph(db)
        elif choice == '6':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

def show_genre_graph(df):
    base_node_size = 3000
    if df.empty or 'Genre' not in df.columns or 'Title' not in df.columns:
        print("❌ No genre or title data to display.")
        return

    df = df.dropna(subset=['Genre', 'Title'])
    df['Genre'] = df['Genre'].str.strip()
    df['Title'] = df['Title'].str.strip()

    genre_counts = df['Genre'].value_counts()
    if genre_counts.empty:
        print("❌ No genres found in the database.")
        return

    G = nx.Graph()

    for genre, count in genre_counts.items():
        G.add_node(genre, type='genre', size=base_node_size + count * 300)

    for _, row in df.iterrows():
        title = row['Title']
        genre = row['Genre']
        G.add_node(title, type='book', size=600)
        G.add_edge(title, genre)

    genre_nodes = [n for n in G.nodes if G.nodes[n]['type'] == 'genre']
    genre_subgraph = G.subgraph(genre_nodes)
    genre_pos = nx.spring_layout(genre_subgraph, seed=42, k=2.0)

    pos = genre_pos.copy()
    for genre in genre_nodes:
        books = [n for n in G.neighbors(genre) if G.nodes[n]['type'] == 'book']
        n_books = len(books)
        if n_books == 0:
            continue

        angle_step = 2 * np.pi / n_books
        radius = 0.1 + 0.05 * min(n_books, 5)

        for i, book in enumerate(books):
            angle = i * angle_step
            x_offset = radius * np.cos(angle)
            y_offset = radius * np.sin(angle)
            pos[book] = (genre_pos[genre][0] + x_offset, genre_pos[genre][1] + y_offset)

    colors_list = list(mcolors.TABLEAU_COLORS.values()) + list(mcolors.CSS4_COLORS.values())
    color_map = {genre: colors_list[i % len(colors_list)] for i, genre in enumerate(genre_counts.index)}

    sizes = [G.nodes[n]['size'] for n in G.nodes()]
    node_colors = [
        color_map[n] if G.nodes[n]['type'] == 'genre'
        else color_map[next(g for g in G.neighbors(n))]
        for n in G.nodes()
    ]

    plt.figure(figsize=(18, 12))
    nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color=node_colors, alpha=0.9)
    nx.draw_networkx_edges(G, pos, width=1.2, alpha=0.3)

    genre_labels = {n: n for n in genre_nodes}
    nx.draw_networkx_labels(G, pos, labels=genre_labels, font_size=10, font_weight='bold')

    for node in G.nodes:
        if G.nodes[node]['type'] == 'book':
            x, y = pos[node]
            plt.text(x, y - 0.05, node, fontsize=8, ha='center', va='top')

    plt.title("Book Genre Graph — Spread Genres, Local Books", fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
