import Buttons.ColorButton;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.lang.*;
import java.util.ArrayList;
import java.util.List;

public class Paint{
    List<ColorButton> colorButtons = new ArrayList<>();

    DrawArea drawArea;


    private void addAllColorButtons() {
        colorButtons.add(new ColorButton( Color.black, drawArea::setPaintColor));
        colorButtons.add(new ColorButton( Color.darkGray, drawArea::setPaintColor));
        colorButtons.add(new ColorButton( Color.lightGray, drawArea::setPaintColor));
        colorButtons.add(new ColorButton( Color.blue, drawArea::setPaintColor));
        colorButtons.add(new ColorButton( Color.cyan, drawArea::setPaintColor));
        colorButtons.add(new ColorButton( Color.magenta, drawArea::setPaintColor));
        colorButtons.add(new ColorButton( Color.red, drawArea::setPaintColor));
        colorButtons.add(new ColorButton( Color.yellow, drawArea::setPaintColor));
        colorButtons.add(new ColorButton( Color.orange, drawArea::setPaintColor));

    }

    public static void main(String[] args) {
        new Paint().show();
    }

    public void show() {
        JFrame frame = new JFrame("MyPaint");
        Container content = frame.getContentPane();
        content.setLayout(new BorderLayout());

        drawArea = new DrawArea();

        content.add(drawArea, BorderLayout.CENTER);

        JPanel colorButtonsPanel = new JPanel();
        addAllColorButtons();

        JPanel controlsPanel = new JPanel();


        colorButtons.forEach(colorButtonsPanel::add);
        content.add(colorButtonsPanel, BorderLayout.SOUTH);

        frame.setSize(1280, 720);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
