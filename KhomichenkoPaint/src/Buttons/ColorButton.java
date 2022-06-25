package Buttons;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ColorButton extends JButton{
    Color color;

    public ColorButton(Color color, SetColorFunc setColor) {
        this.color = color;
        this.setBackground(color);
        this.setPreferredSize(new Dimension(40, 40));

        this.addActionListener(e -> setColor.setColor(this.color));


    }

}
