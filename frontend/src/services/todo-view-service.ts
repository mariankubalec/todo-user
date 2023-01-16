export function getFormattedDateTime(input: string): string {
  if (input) {
    return input.substring(0, input.indexOf('T'));
  } else {
    return '';
  }
}