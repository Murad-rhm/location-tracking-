o
    2��b�  �                   @   s�  d dl Z d dlZd dlZd dlZd dlZe�d� dd� Zdd� Zdd� Zd	Z	d
Z
dZdZdZdZdZdZdZdZdZdZdZdZdZdZdZdZdZdZdZdZdZd Z d!Z!	 e�  e�  e"ed# � e"d$� e#e	d% e e	 �Z$e$d&kr�e�  e�%d'� e#ed( e	 � e�d� nIe$d)kr�e�  e�  e"d*� e#ed+ e	 �Z&e"e� d,e&� d-�Z'e �(e'�Z)e)�*� Z+e�e+� e#ed. e	 �Z,e�d� ne"ed/ e	 � e�%d0� qX)1�    N�clearc                   C   s   t �d� t �d� d S )Nzgem install rubyzgem install lolcat��os�system� r   r   �location_tracking.py�basic   s   
r   c                   C   s   t �d� td� d S )Nzlolcat logo.txt�

)r   r   �printr   r   r   r   �logo   s   
r   c                   C   s   t �d� d S )Nzlolcat logo2.txtr   r   r   r   r   �logo2   s   r   z[0mz[0;30mz[0;31mz[0;32mz[0;33mz[0;34mz[0;35mz[0;36mz[0;37mz[1;30mz[1;31mz[1;32mz[1;33mz[1;34mz[1;35mz[1;36mz[1;37mz[40mz[41mz[42mz[43mz[44mz[45mz[46mz[47mTz.
[1] install requirement:
[2] location track:
z1 must installed...
z[?] choose: �1�   z[>]Enter...�2r	   z[?]Enter victims ip :zhttps://ipapi.co/z/json/u   [∆]Enter for try again?!z[!!] invalid :g{�G�zt?)-Zrequests�timer   �sysZpprintr   r   r   r   �coZblackZredZgreenZyellowZblueZpurpleZcyanZwhiteZbblackZbredZbgreenZbyellowZbblueZbpurpleZbcyanZbwhiteZon_blackZon_redZon_greenZ	on_yellowZon_blueZ	on_purpleZon_cyanZon_whiter
   �inputZinn�sleepZip�url�getZreqZjson�info�ir   r   r   r   �<module>   sx   




�