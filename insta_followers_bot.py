# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 02:05:41 2020

@author: shivj
"""

from selenium import webdriver
from time import sleep

class insta_bot:
    def __init__(self, user,pwd):
        self.user=user
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(user)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pwd)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(8)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(4)
        
    
    def get_followers(self):
        self.driver.get(f"https://www.instagram.com/{self.user}")
        sleep(5)
        self.driver.find_element_by_xpath(f"//a[contains(@href,'/{self.user}/followers/')]").click()
        sleep(2)
        
        
    def get_following(self):
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        sleep(2)
        self.driver.find_element_by_xpath(f"//a[contains(@href,'/{self.user}/following/')]").click()
        sleep(2)
    
    def get_names(self):
        scroll_box=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht=0,1
        while last_ht != ht:
            last_ht = ht
            sleep(5)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        link=scroll_box.find_elements_by_tag_name('a')
        names=[name.text for name in link if name.text !=""]
        return names
    
    def show_not_following_back(self):
        self.get_followers()
        followers=self.get_names()
        self.get_following()
        following=self.get_names()
        not_following_back=[users for users in following if users not in followers]
        print(not_following_back)
        
        
my_bot=insta_bot("shivjethi", "Password123")
my_bot.show_not_following_back()
