import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from textblob import TextBlob

driver_path="C:/Users/Admin/Desktop/pythonpractice/chromedriver.exe"
driver=wd.Chrome(executable_path=driver_path)
driver.get("https://www.youtube.com/watch?v=aPTnq_1hWDE")
wait=WebDriverWait(driver,20)
time.sleep(20)
target_comments=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div#contents ytd-comment-thread-renderer ytd-comment-renderer#comment")))
total_polarity=0
count_comments=0
total_subjectivity=0
for i in target_comments:
    target_comment_one=i.find_element(By.CSS_SELECTOR,"yt-formatted-string#content-text")
    analysis=TextBlob(target_comment_one.text)
    print(target_comment_one.text)
    print("polarity value", analysis.sentiment.polarity,"subjectivity value",analysis.sentiment.subjectivity)
    print(total_subjectivity)
    print(total_polarity)
    total_polarity=total_polarity+analysis.sentiment.polarity
    count_comments=count_comments+1
    total_subjectivity=total_subjectivity+analysis.sentiment.subjectivity
overall_polarity=total_polarity/count_comments
overall_subjectivity=total_subjectivity/count_comments
print(overall_polarity)
if overall_polarity>=0.2:
    print("its a positive video")
elif overall_polarity>=-0.2 and overall_polarity<0.2:
    print("it is neutral")
elif overall_polarity<-0.2:
    print("it is negative")

if overall_polarity>0.5:
    print("its subjective")

elif overall_polarity<=0.5:
    print("it is objective")



