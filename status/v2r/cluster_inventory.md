# V2R cluster inventory

2026-09-25T16:40:59.457074+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318683668480 available bytes; 82.22% used; 112476339 free inodes.

server1 `/home`: 318683668480 available bytes; 82.22% used; 112476339 free inodes.

server1 `/tmp`: 318683668480 available bytes; 82.22% used; 112476339 free inodes.

server1 `/var/tmp`: 318683668480 available bytes; 82.22% used; 112476339 free inodes.

server1 `/mnt/raid5`: 363879071744 available bytes; 98.33% used; 337544347 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23099424768 available bytes; 98.71% used; 110407930 free inodes.

server2 `/home`: 23099424768 available bytes; 98.71% used; 110407930 free inodes.

server2 `/tmp`: 23099424768 available bytes; 98.71% used; 110407930 free inodes.

server2 `/var/tmp`: 23099424768 available bytes; 98.71% used; 110407930 free inodes.

server2 `/mnt/raid5`: 316408549376 available bytes; 97.81% used; 445069633 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84395171840 available bytes; 95.29% used; 114152643 free inodes.

server3 `/home`: 84395171840 available bytes; 95.29% used; 114152643 free inodes.

server3 `/data`: 133790330880 available bytes; 98.15% used; 225805548 free inodes.

server3 `/tmp`: 84395171840 available bytes; 95.29% used; 114152643 free inodes.

server3 `/var/tmp`: 84395171840 available bytes; 95.29% used; 114152643 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105635799040 available bytes; 94.11% used; 114349643 free inodes.

server4 `/home`: 105635799040 available bytes; 94.11% used; 114349643 free inodes.

server4 `/data`: 230003752960 available bytes; 96.82% used; 224933774 free inodes.

server4 `/tmp`: 105635799040 available bytes; 94.11% used; 114349643 free inodes.

server4 `/var/tmp`: 105635799040 available bytes; 94.11% used; 114349643 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
