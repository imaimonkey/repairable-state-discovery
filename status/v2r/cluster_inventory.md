# V2R cluster inventory

2026-09-27T04:03:17.478614+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315075477504 available bytes; 82.42% used; 112443048 free inodes.

server1 `/home`: 315075477504 available bytes; 82.42% used; 112443048 free inodes.

server1 `/tmp`: 315075477504 available bytes; 82.42% used; 112443048 free inodes.

server1 `/var/tmp`: 315075477504 available bytes; 82.42% used; 112443048 free inodes.

server1 `/mnt/raid5`: 636758376448 available bytes; 97.08% used; 337401269 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17632976896 available bytes; 99.02% used; 110365007 free inodes.

server2 `/home`: 17632976896 available bytes; 99.02% used; 110365007 free inodes.

server2 `/tmp`: 17632976896 available bytes; 99.02% used; 110365007 free inodes.

server2 `/var/tmp`: 17632976896 available bytes; 99.02% used; 110365007 free inodes.

server2 `/mnt/raid5`: 577726664704 available bytes; 96.01% used; 444882523 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78697074688 available bytes; 95.61% used; 114062928 free inodes.

server3 `/home`: 78697074688 available bytes; 95.61% used; 114062928 free inodes.

server3 `/data`: 1335185358848 available bytes; 81.55% used; 225759675 free inodes.

server3 `/tmp`: 78697074688 available bytes; 95.61% used; 114062928 free inodes.

server3 `/var/tmp`: 78697074688 available bytes; 95.61% used; 114062928 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111018778624 available bytes; 93.80% used; 114372943 free inodes.

server4 `/home`: 111018778624 available bytes; 93.80% used; 114372943 free inodes.

server4 `/data`: 382181531648 available bytes; 94.72% used; 224780779 free inodes.

server4 `/tmp`: 111018778624 available bytes; 93.80% used; 114372943 free inodes.

server4 `/var/tmp`: 111018778624 available bytes; 93.80% used; 114372943 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
