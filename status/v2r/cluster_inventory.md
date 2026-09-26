# V2R cluster inventory

2026-09-26T08:27:10.426935+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318747779072 available bytes; 82.22% used; 112475803 free inodes.

server1 `/home`: 318747779072 available bytes; 82.22% used; 112475803 free inodes.

server1 `/tmp`: 318747779072 available bytes; 82.22% used; 112475803 free inodes.

server1 `/var/tmp`: 318747779072 available bytes; 82.22% used; 112475803 free inodes.

server1 `/mnt/raid5`: 219112718336 available bytes; 98.99% used; 337538961 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22317170688 available bytes; 98.76% used; 110403906 free inodes.

server2 `/home`: 22317170688 available bytes; 98.76% used; 110403906 free inodes.

server2 `/tmp`: 22317170688 available bytes; 98.76% used; 110403906 free inodes.

server2 `/var/tmp`: 22317170688 available bytes; 98.76% used; 110403906 free inodes.

server2 `/mnt/raid5`: 255273791488 available bytes; 98.24% used; 445024803 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82678767616 available bytes; 95.39% used; 114110811 free inodes.

server3 `/home`: 82678767616 available bytes; 95.39% used; 114110811 free inodes.

server3 `/data`: 123913015296 available bytes; 98.29% used; 225828941 free inodes.

server3 `/tmp`: 82678767616 available bytes; 95.39% used; 114110811 free inodes.

server3 `/var/tmp`: 82678767616 available bytes; 95.39% used; 114110811 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106064232448 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106064232448 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89376854016 available bytes; 98.76% used; 224883408 free inodes.

server4 `/tmp`: 106064232448 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106064232448 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
