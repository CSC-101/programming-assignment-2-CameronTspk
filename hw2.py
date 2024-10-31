from data import *

# Part 1
#Function creates the top most left point and bottom most left point for a rectangle
# from an input of two points that may or may not be those points
def create_rectangle(point1:Point,point2:Point)-> Rectangle:
#Rectangle(Point(x,y),Point(x,y)
    ##finding smallest value of x from given points and assigning it to topleft point and the opposite to bottom right
    if point1.x < point2.x:
        top_left_x = point1.x
        bottom_right_x = point2.x
    else:
        top_left_x = point2.x
        bottom_right_x = point1.x
    #finding largest value of y from given points and assigning it to topleft point and the opposite to bottom right
    if point1.y > point2.y:
        top_left_y = point1.y
        bottom_right_y = point2.y
    else:
        top_left_y = point2.y
        bottom_right_y = point1.y
    #assigned values are then used to create points for the topleft and bottom right of the rectangle
    top_left = Point(top_left_x,top_left_y)
    bottom_right = Point(bottom_right_x, bottom_right_y)
    created_rectangle = Rectangle(top_left,bottom_right)
    return created_rectangle

# Part 2
def shorter_duration_than(time1:Duration, time2:Duration) -> bool:
    #creates two values for which the duration of the songs can be easily represented
    #instead of comparing minutes and seconds we now only compare the total seconds
    time1_total = (time1.minutes * 60) + time1.seconds
    time2_total = (time2.minutes * 60) + time2.seconds
    #returns a boolean value of True when the first song is less than the second and False otherwise
    return time1_total < time2_total


# Part 3
def song_shorter_than(song_list: list[Song], max_length: Duration) -> list[Song]:
    #Create a list for songs of short enough length to be stored
    short_songs = []
    #testing that for each song in the list passed in whether it is less than the max_length testing parameter
    for song in song_list:
        #easy to compare just as seconds so that one is longer or not
        song_length = (song.duration.minutes*60 +song.duration.seconds)
        max_length_seconds = max_length.minutes * 60 + max_length.seconds
        #if the song is less than the tested duration then that song is then appended to the list
        if song_length < max_length_seconds:
            short_songs.append(song)
    return short_songs


# Part 4
def playlist_length(play_list: list[Song], order_songs: list[int]) -> Duration:
    total_minutes = 0
    total_seconds = 0
    for index in order_songs:
        if 0 <= index < len(play_list):  # Check if the index is within the range
            current_song = play_list[index]

            total_minutes += current_song.duration.minutes
            total_seconds += current_song.duration.seconds

        # Convert any excess seconds to minutes
    total_minutes += total_seconds // 60
    total_seconds = total_seconds % 60
    total_time = Duration(total_minutes, total_seconds)
    return total_time


# Part 5
def validate_route(city_links:list[list[str]],route_city_list:list[str]) -> bool:

#create a function which will test edge cases first route list = 0 or 1
#so that if o occurs its true and if only one name occurs its true
#now if list of two or greater we iterate in pairs of two and evaluate wether any pairing occurs in the city list
    if len(route_city_list) < 2:
        print("less than 2")
        return True
    else:
        j=0
        for i in range(len(route_city_list) - 1):
            city_one = route_city_list[j]
            city_two = route_city_list[j+1]
            if not [city_one, city_two] in city_links:
                return False
            j += 1
        return True





print(validate_route(city_list,route_list))

#def longest_repetition(evaluated_list: list[int]) -> Optional[int]:
    #start evaluating through the list say when the following number is equal we increase the length by 1 and when it's not we
# create a new list storing the higher one after