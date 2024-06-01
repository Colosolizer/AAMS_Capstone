import 'package:flutter/material.dart';

class Fishstats extends StatelessWidget {
  const Fishstats({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 350,
      height: 200,
      child: Column(
        children: [
          Row(
            children: [_RowItem('Swimming Pattern:'),],
          ),
          Row(
            children: [_RowItem('Feeding Pattern: '),],
          )
        ],
      ),
    );
  }
}

class _RowItem extends StatelessWidget {
  final String title;
  const _RowItem(this.title);
  @override
  Widget build(BuildContext context) {
    return Text(
      title,
      style: TextStyle(fontSize: 30),
    );
  }
}
