import 'package:flutter/material.dart';

class FishEmoji extends StatelessWidget {
  const FishEmoji({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 200,
      child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(
              'FISH EMOTION',
              style: TextStyle(
                  fontWeight: FontWeight.w200, height: 0.9, fontSize: 40),
            ),
            SizedBox(
              height: 10,
            ),
            SizedBox(
              height: 100,
              width: 200,
              child: Image.asset('happy-face.png'),
            ),
          ]),
    );
  }
}
