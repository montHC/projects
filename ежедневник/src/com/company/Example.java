package com.company;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;



import javax.swing.*;

public class Example extends JFrame
{
    public static void run()
    {

        final JFrame window = new JFrame("Ежедневник");
        JTextArea textArea = new JTextArea("Список дел", 10, 10);
        JPanel panel = new JPanel();

        JButton Button = new JButton("сохранить");
        ImageIcon img = new ImageIcon("java.png");
        window.setIconImage(img.getImage());


     String[] days =  { "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"};
        JComboBox comboBox = new JComboBox(days);

        window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


        panel.add(comboBox);
        panel.add(textArea);
        panel.add(Button);


        //Добавим панель в окно
        window.getContentPane().add(panel);

        window.pack();

        //Разместим программу по центру
        window.setLocationRelativeTo(null);
        window.setVisible(true);
        comboBox.addActionListener(new ActionListener(){

            @Override
            public void actionPerformed(ActionEvent e) {
int num=comboBox.getSelectedIndex();
switch (num){
    case 0: textArea.setText("сдеалть матан");break;
    case 1: textArea.setText("Купить подарок\n "+
    "Сделать ООП");break;
    case 2: textArea.setText("");break;
    case 3: textArea.setText("сделать дизайн");break;
    case 4: textArea.setText("почитать книгу");break;
    case 5: textArea.setText("купить хлеб");break;
    case 6: textArea.setText("нарисовать портрет");break;

            }}
        });
     comboBox.setSelectedIndex(-1);


    }}