import "package:flutter/material.dart";
import "package:the_basics/widgets/centered_view/centered_view.dart";
import "package:the_basics/widgets/fish_emoji/fish_emoji.dart";
import "package:the_basics/widgets/navigation_bar/navigation_bar.dart"
    as custom;
import 'package:the_basics/widgets/fishstats/fishstats.dart';
import 'package:the_basics/widgets/FishDetector/FishDetector.dart';

class HomeView extends StatelessWidget {
  const HomeView({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        body: CenteredView(
          child: Column(
            children: <Widget>[
              custom.NavigationBar(),
              Expanded(
                  child: Row(
                children: [
                  FishDetector(),
                  Expanded(
                      child: Center(
                    child: Column(children: <Widget>[Fishstats(),FishEmoji()])
                  ))
                ],
              ))
            ],
          ),
        ));
  }
}
