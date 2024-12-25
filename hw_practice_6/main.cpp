#include <SFML/Graphics.hpp>

using namespace sf;

int main()
{
    int cellSize = 50;
    const int gridSize = 10;
    int counter = 1;

    RenderWindow window(VideoMode(500, 500), "Cube");

    RectangleShape cells[gridSize][gridSize];

    while (window.isOpen())
    {

        Event event;
        while (window.pollEvent(event))
        {
            if (event.type == Event::Closed)
                window.close();
        }

        for (int x = 0; x < gridSize; x++) {
            for (int y = 0; y < gridSize; y++) {
                cells[x][y].setSize(Vector2f(cellSize - 2, cellSize - 2));
                cells[x][y].setPosition(x * cellSize, y * cellSize);
                cells[x][y].setFillColor(Color::Black);
                cells[x][y].setOutlineColor(Color::White);
                cells[x][y].setOutlineThickness(1);
                window.draw(cells[x][y]);
            }
        }

        for (int x = 0; x < gridSize; x++) {
            if (x % 2 != 0) {
                for (int y = 0; y < gridSize; y++) {
                    if (y >= (gridSize - x)) {
                        cells[y][x].setFillColor(Color::Green);
                        window.draw(cells[y][x]);
                    }
                }
                counter+= 2;
            }
        }

        window.display();
    }

    return 0;
}