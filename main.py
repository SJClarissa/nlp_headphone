import pandas as pd
import numpy as np
from flask import Flask, request, render_template, Response
import sys
from LDA_Pointer.LDA_Pointer import *

app_lda = Flask('App_LDA')
lda1 = LDA_Pointer('2019','7')
lda2 = LDA_Pointer('2019','7')

# print(year1, cat1, year2, cat2)

@app_lda.route('/')
def main():
    return render_template('main.html')

@app_lda.route('/default')
def default():
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')

@app_lda.route('/year1_2019')
def year1_2019():
    lda1.set_year('2019')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')

@app_lda.route('/year1_2018')
def year1_2018():
    lda1.set_year('2018')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')
    
@app_lda.route('/year1_2017')
def year1_2017():
    lda1.set_year('2017')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')
    
@app_lda.route('/year1_2016')
def year1_2016():
    lda1.set_year('2016')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')
    
@app_lda.route('/year1_2015')
def year1_2015():
    lda1.set_year('2015')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')
    
@app_lda.route('/year1_2014')
def year1_2014():
    lda1.set_year('2014')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')
    
@app_lda.route('/year1_2013')
def year1_2013():
    lda1.set_year('2013')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')
    
@app_lda.route('/year1_2012')
def year1_2012():
    lda1.set_year('2012')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')
    
@app_lda.route('/year1_2011')
def year1_2011():
    lda1.set_year('2011')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')
    
@app_lda.route('/year1_2010')
def year1_2010():
    lda1.set_year('2010')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')

@app_lda.route('/year2_2019')
def year2_2019():
    lda2.set_year('2019')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')

@app_lda.route('/year2_2018')
def year2_2018():
    lda2.set_year('2018')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')
    
@app_lda.route('/year2_2017')
def year2_2017():
    lda2.set_year('2017')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')
    
@app_lda.route('/year2_2016')
def year2_2016():
    lda2.set_year('2016')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')
    
@app_lda.route('/year2_2015')
def year2_2015():
    lda2.set_year('2015')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')
    
@app_lda.route('/year2_2014')
def year2_2014():
    lda2.set_year('2014')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')
    
@app_lda.route('/year2_2013')
def year2_2013():
    lda2.set_year('2013')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')
    
@app_lda.route('/year2_2012')
def year2_2012():
    lda2.set_year('2012')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')
    
@app_lda.route('/year2_2011')
def year2_2011():
    lda2.set_year('2011')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')
    
@app_lda.route('/year2_2010')
def year2_2010():
    lda2.set_year('2010')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')

@app_lda.route('/cat1_3')
def cat1_3():
    lda1.set_category_num('3')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')


@app_lda.route('/cat1_5')
def cat1_5():
    lda1.set_category_num('5')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')
    
@app_lda.route('/cat1_7')
def cat1_7():
    lda1.set_category_num('7')
    return render_template('ldavis_prepared_'+ lda1.get_year() + '_' + lda1.get_category_num() + '.html')

@app_lda.route('/cat2_3')
def cat2_3():
    lda2.set_category_num('3')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')

@app_lda.route('/cat2_5')
def cat2_5():
    lda2.set_category_num('5')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')

@app_lda.route('/cat2_7')
def cat2_7():
    lda2.set_category_num('7')
    return render_template('ldavis_prepared_'+ lda2.get_year() + '_' + lda2.get_category_num() + '.html')

if __name__ == '__main__':
    app_lda.run(debug=True)
    #app_lda.run(host='0.0.0.0')
    