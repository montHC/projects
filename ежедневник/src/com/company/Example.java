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
        
        window.getContentPane().add(panel);

        window.pack();

        window.setLocationRelativeTo(null);
        window.setVisible(true);
        comboBox.addActionListener(new ActionListener(){

            @Override
            public void actionPerformed(ActionEvent e) {
int num=comboBox.getSelectedIndex();
switch (num){
    case 0: textArea.setText("Запишите дело");break;
    case 1: textArea.setText("Запишите дело\n "+
    "Запишите дело");break;
    case 2: textArea.setText("Запишите дело");break;
    case 3: textArea.setText("Запишите дело");break;
    case 4: textArea.setText("Запишите дело");break;
    case 5: textArea.setText("Запишите дело");break;
    case 6: textArea.setText("Запишите дело");break;

            }}
        });
     comboBox.setSelectedIndex(-1);


    }}