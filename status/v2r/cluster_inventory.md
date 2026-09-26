# V2R cluster inventory

2026-09-26T08:53:08.465024+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318746308608 available bytes; 82.22% used; 112475809 free inodes.

server1 `/home`: 318746308608 available bytes; 82.22% used; 112475809 free inodes.

server1 `/tmp`: 318746308608 available bytes; 82.22% used; 112475809 free inodes.

server1 `/var/tmp`: 318746308608 available bytes; 82.22% used; 112475809 free inodes.

server1 `/mnt/raid5`: 219048652800 available bytes; 99.00% used; 337538826 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22323613696 available bytes; 98.75% used; 110403909 free inodes.

server2 `/home`: 22323613696 available bytes; 98.75% used; 110403909 free inodes.

server2 `/tmp`: 22323613696 available bytes; 98.75% used; 110403909 free inodes.

server2 `/var/tmp`: 22323613696 available bytes; 98.75% used; 110403909 free inodes.

server2 `/mnt/raid5`: 255305940992 available bytes; 98.24% used; 445024353 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82671423488 available bytes; 95.39% used; 114110810 free inodes.

server3 `/home`: 82671423488 available bytes; 95.39% used; 114110810 free inodes.

server3 `/data`: 123897921536 available bytes; 98.29% used; 225828399 free inodes.

server3 `/tmp`: 82671423488 available bytes; 95.39% used; 114110810 free inodes.

server3 `/var/tmp`: 82671423488 available bytes; 95.39% used; 114110810 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106063437824 available bytes; 94.08% used; 114348133 free inodes.

server4 `/home`: 106063437824 available bytes; 94.08% used; 114348133 free inodes.

server4 `/data`: 89347792896 available bytes; 98.77% used; 224883353 free inodes.

server4 `/tmp`: 106063437824 available bytes; 94.08% used; 114348133 free inodes.

server4 `/var/tmp`: 106063437824 available bytes; 94.08% used; 114348133 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
