# V2R cluster inventory

2026-09-25T19:30:43.205793+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318728323072 available bytes; 82.22% used; 112476326 free inodes.

server1 `/home`: 318728323072 available bytes; 82.22% used; 112476326 free inodes.

server1 `/tmp`: 318728323072 available bytes; 82.22% used; 112476326 free inodes.

server1 `/var/tmp`: 318728323072 available bytes; 82.22% used; 112476326 free inodes.

server1 `/mnt/raid5`: 370861101056 available bytes; 98.30% used; 337540793 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23096758272 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23096758272 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23096758272 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23096758272 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 312032591872 available bytes; 97.84% used; 445064428 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84384985088 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84384985088 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 129276108800 available bytes; 98.21% used; 225808572 free inodes.

server3 `/tmp`: 84384985088 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84384985088 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5', '6'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105674756096 available bytes; 94.10% used; 114349582 free inodes.

server4 `/home`: 105674756096 available bytes; 94.10% used; 114349582 free inodes.

server4 `/data`: 229615525888 available bytes; 96.83% used; 224929906 free inodes.

server4 `/tmp`: 105674756096 available bytes; 94.10% used; 114349582 free inodes.

server4 `/var/tmp`: 105674756096 available bytes; 94.10% used; 114349582 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
