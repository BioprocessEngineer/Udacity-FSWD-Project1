import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <link href="https://fonts.googleapis.com/css?family=Slabo+27px" rel="stylesheet">
    <title>Bioprocess Engineer's Favorite Movies</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
    body {
    padding-top: 80px;
    background-color: #ffffff;
    font-family: 'Georgia', serif;
    }

    h2  {
    font-family: "Slabo 27px", serif;
    font-size: 150%;
    font-weight: bold;
    line-height; 80%;
    text-align: center;
    }

    p {
    font-size: 120%;
    color:  #404040;
    font-family: "Slabo 27px", sans-serif;
    }

    p.type {
    font-weight: bold;
    inline-height: 80%;
    margin-top: 20px;
    margin-bottom: 0px;
    }


    #about {
    display: inline;
    border: 2px solid #333333;
    vertical-align: 80%;
    font-size: 50%;
    padding: 0.1%;
    color: #333333;
    }

    #about:hover {
    display: inline;
    border: 2px solid white;
    vertical-align: 80%;
    font-size: 50%;
    padding: 0.1%;
    color: white;
    cursor: pointer;
    }

    #trailer .modal-dialog, #about-modal .modal-dialog {
    margin-top: 200px;
    width: 640px;
    height: 480px;
    }

    .hanging-close {
    position: absolute;
    top: -12px;
    right: -12px;
    z-index: 9001;
    }

    #trailer-video {
    width: 100%;
    height: 100%;
    }

    .movie-tile, .info-tile {
    width: 220px;
    height: 100%;
    position: absolute;
    margin-left: auto;
    margin-right: auto;
    left: 0;
    right: 0;
    font-family: "Slabo 27px", sans-serif;
    }

    .movie-tile{
    z-index: 0;            
    }


    .scale-media {
    padding-bottom: 56.25%;
    position: relative;
    }

    .scale-media iframe {
    border: none;
    height: 100%;
    position: absolute;
    width: 100%;
    left: 0;
    top: 0;
    background-color: white;
    }

    .navbar-custom {
    height: 8%;
    background-color: black; 
    border-bottom-color: #a6a6a6;
    border-bottom-width: 5px;
    }

    .navbar-brand:hover,
    .navbar-brand {
    width: 100%; 
    color: white;
    font-size: 200%;
    }

    .info-tile {
    z-index: 0;
    background-color: #f2f2f2;
    font-size: 100%;
    height: 342px;
    opacity: 0;
    transition: all 0.5s ease;
    line-height: 130%;
    }

    .info-tile:hover {
    z-index: 1;
    opacity: 1;
    transition: all 0.5s ease;
    }

    .movie-block {
    position: relative;
    height: 400px;
    padding: 10px;
    }

    p.play-trailer:hover {
    cursor: pointer;
    color:  #009933;
    }

    </style>
    
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, #trailoer', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.play-trailer', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

     
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-block').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
    
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <div class="modal" id="about-modal">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="about-text" style="margin: 5%; text-align: justify; font-size: 100%; line-height: 150%;">
          <h2>About Bioprocess Engineer</h2>
          <p>I'm currently working in a major human vaccine company in Canada as a Bioprocess Engineer. However after working in this industry for about 2 and half years, I seem to be able to foresee my entire career in the next 30 years.
          Also the excessive supply of biotech talents and limited human resource demand make the biotech career path a bit gloomy going forward. So I started to think about making a career change and the first ideas come to my mind are
          computer and design because I can still remember the joy and excitement I had when I got my first computer and spent days on OS installation, Windows Theme customization, setting up discussing board, etc.</p>
          <p>After doing a bit research, I found that the Full Stack Web Developer Nanodegree at Udaciy most interesting to me and at the same time Web Developer seems to be a more accessible (maybe I'm naive on this point) choice when
          making such a change for myself. After all, I immediately feel the excitement again when dointg the coueses and projects in thie Nanodegree Program. I like it a lot as I find the content offered in the courses is very applicable
          and the also the instructions provided by the lecturer are very concise and clear.</p>
          <p>Next I am planning to finish this course in 2-3 months and trying to put down my first step in the Web by this Christmas.</p>
          <p>My Regards to the Udacity Team,</p>
          <p>Jian</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
    <div class="navbar navbar-custom navbar-fixed-top" role="navigation" style="margin:auto; width:100%;">
      <div class="container" style="margin: auto; width: 100%; height: 100%;">
        <div class="navbar-header" align="center" style="width: 100%; height: 100%;">
          <h1 class="navbar-brand" style="height: 100%; margin: auto;">
          Bioprocess Engineer's<p id="about" data-toggle="modal" data-target="#about-modal">about</p>Favorite Movies</h1>
        </div>
      </div>
    </div>
  </div>
    <div class="container" style="vertical-align: middle;">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''

<div class="col-sm-6 col-md-6 col-lg-4 movie-block text center">

<div class="movie-tile text-center">
    <img src="{poster_image_url}" width="220" height="342">
</div>

<div class="info-tile text-center">
    <h2>{movie_title}</h2>
    <p class="type">Year</p>
    <p>{movie_year}</p>
    <p class="type">Director</p>
    <p>{movie_director}</p>
    <p class="type">IMDB &#9733Rating</p>
    <p>{movie_rating}</p>
    <p class="play-trailer" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer"><b>&#9654Play Trailer</b></p>
</div>

</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:

    # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_year=movie.year,
            movie_director=movie.director,
            movie_rating=movie.rating
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('bioprocess_engineer.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
    movie_tiles = create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
