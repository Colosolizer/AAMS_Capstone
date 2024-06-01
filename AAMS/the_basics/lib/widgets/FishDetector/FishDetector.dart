import 'package:flutter/material.dart';
import 'package:video_player/video_player.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class FishDetector extends StatefulWidget {
  const FishDetector({Key? key}) : super(key: key);

  @override
  _FishDetectorState createState() => _FishDetectorState();
}

class _FishDetectorState extends State<FishDetector> {
  VideoPlayerController? _controller;
  int _numFish = 0;

  @override
  void initState() {
    super.initState();
    _controller = VideoPlayerController.network(
      'http://localhost:5000/video_feed',
    )..initialize().then((_) {
        setState(() {});
        _controller!.play();
        _controller!.setLooping(true);
      });

    _fetchNumFish();
  }

  Future<void> _fetchNumFish() async {
    final response = await http.get(Uri.parse('http://localhost:5000/num_fish'));
    if (response.statusCode == 200) {
      setState(() {
        _numFish = json.decode(response.body)['num_fish'];
      });
    } else {
      throw Exception('Failed to load number of fish');
    }
  }

  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 200,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          if (_controller != null && _controller!.value.isInitialized)
            AspectRatio(
              aspectRatio: _controller!.value.aspectRatio,
              child: VideoPlayer(_controller!),
            )
          else
            Center(child: CircularProgressIndicator()),
          SizedBox(height: 20),
          Text(
            'Number of fish detected: $_numFish',
            style: TextStyle(fontSize: 20),
          ),
          SizedBox(height: 10),
          FloatingActionButton(
            onPressed: _fetchNumFish,
            tooltip: 'Refresh',
            child: Icon(Icons.refresh),
          ),
        ],
      ),
    );
  }
}
