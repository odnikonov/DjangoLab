var groupmates = [
    {
    "name": "?????",
    "group": "912-2",
    "age": 19,
    "marks": [4, 3, 5, 5, 4]
    },
    {
    "name": "????",
    "group": "912-1",
    "age": 18,
    "marks": [3, 2, 3, 4, 3]
    },
    {
    "name": "????",
    "group": "912-2",
    "age": 19,
    "marks": [3, 5, 4, 3, 5]
    },
    {
    "name": "????",
    "group": "912-1",
    "age": 18,
    "marks": [5, 5, 5, 4, 5]
    }
];   
var rpad = function(str, length) {
    str = str+""; // преобразование в ѝтроку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец ѝтроки
    return str; // когда вѝе пробелы добавлены, возвратить ѝтроку
};
var printStudents = function(students){
    console.log(
        rpad("Имѝ", 15),
        rpad("Фамилиѝ", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i<=students.length-1; i++){
        // в цикле выводитѝѝ каждый ѝкземплѝр ѝтудента
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавлѝетѝѝ пуѝтаѝ ѝтрока в конце вывода
};
//printStudents(groupmates);
var printStudentsForGroup = function(students, group){
    console.log(
        rpad("Имѝ", 15),
        rpad("Фамилиѝ", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i<=students.length-1; i++){
        if (students[i]['group'] == group){
            console.log(
                rpad(students[i]['name'], 15),
                rpad(students[i]['surname'], 15),
                rpad(students[i]['group'], 8),
                rpad(students[i]['marks'], 20)
            );
        }
    }
    console.log('\n'); // добавлѝетѝѝ пуѝтаѝ ѝтрока в конце вывода
};
//var group = prompt('Input Group');
//printStudentsForGroup(groupmates, group);