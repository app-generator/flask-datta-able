# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import subprocess

import pyautogui
import os
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route("/index")
@login_required
def index():
    files = display_file()
    return render_template("home/index.html", segment="index",files=files)


@blueprint.route("/<template>")
@login_required
def route_template(template):
    try:
        if not template.endswith(".html"):
            template += ".html"

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template("home/page-404.html"), 404

    except:
        return render_template("home/page-500.html"), 500


@blueprint.route("/open_presentation", methods=["POST"])
def open_slideshow():
    powerpoint_path = "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE"
    file = request.files["file_path"]
    if file:
        file.save(f"./files/{file.filename}")
        try:
            file_path = "./files/"+file.filename
            # subprocess.Popen([powerpoint_path, "C:/Users/Asus/Desktop/python/app/test.pptx"])
            subprocess.Popen([powerpoint_path, file_path])
            pyautogui.sleep(2)
            pyautogui.press("f5")
            files = display_file()
            return render_template("home/index.html", segment="index", files=files)

        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "no file selected"

@blueprint.route("/display_filenames")
def display_file():
    files = os.listdir("files")
    return files



# Helper - Extract current page name from request
def get_segment(request):
    try:
        segment = request.path.split("/")[-1]

        if segment == "":
            segment = "index"

        return segment

    except:
        return None
