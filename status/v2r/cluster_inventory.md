# V2R cluster inventory

2026-09-27T03:55:40.022711+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315075260416 available bytes; 82.42% used; 112443035 free inodes.

server1 `/home`: 315075260416 available bytes; 82.42% used; 112443035 free inodes.

server1 `/tmp`: 315075260416 available bytes; 82.42% used; 112443035 free inodes.

server1 `/var/tmp`: 315075260416 available bytes; 82.42% used; 112443035 free inodes.

server1 `/mnt/raid5`: 636785909760 available bytes; 97.08% used; 337401379 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17624596480 available bytes; 99.02% used; 110365009 free inodes.

server2 `/home`: 17624596480 available bytes; 99.02% used; 110365009 free inodes.

server2 `/tmp`: 17624596480 available bytes; 99.02% used; 110365009 free inodes.

server2 `/var/tmp`: 17624596480 available bytes; 99.02% used; 110365009 free inodes.

server2 `/mnt/raid5`: 577936003072 available bytes; 96.01% used; 444881802 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 78696939520 available bytes; 95.61% used; 114062933 free inodes.

server3 `/home`: 78696939520 available bytes; 95.61% used; 114062933 free inodes.

server3 `/data`: 1335284097024 available bytes; 81.55% used; 225760825 free inodes.

server3 `/tmp`: 78696939520 available bytes; 95.61% used; 114062933 free inodes.

server3 `/var/tmp`: 78696939520 available bytes; 95.61% used; 114062933 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111027359744 available bytes; 93.80% used; 114372943 free inodes.

server4 `/home`: 111027359744 available bytes; 93.80% used; 114372943 free inodes.

server4 `/data`: 382180016128 available bytes; 94.72% used; 224780789 free inodes.

server4 `/tmp`: 111027359744 available bytes; 93.80% used; 114372943 free inodes.

server4 `/var/tmp`: 111027359744 available bytes; 93.80% used; 114372943 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
