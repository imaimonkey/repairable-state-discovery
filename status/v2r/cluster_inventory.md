# V2R cluster inventory

2026-09-27T04:41:24.157846+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314905804800 available bytes; 82.43% used; 112443034 free inodes.

server1 `/home`: 314905804800 available bytes; 82.43% used; 112443034 free inodes.

server1 `/tmp`: 314905804800 available bytes; 82.43% used; 112443034 free inodes.

server1 `/var/tmp`: 314905804800 available bytes; 82.43% used; 112443034 free inodes.

server1 `/mnt/raid5`: 636059324416 available bytes; 97.08% used; 337400333 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17628385280 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17628385280 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17628385280 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17628385280 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 576488402944 available bytes; 96.02% used; 444879050 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 78696763392 available bytes; 95.61% used; 114062936 free inodes.

server3 `/home`: 78696763392 available bytes; 95.61% used; 114062936 free inodes.

server3 `/data`: 1335049687040 available bytes; 81.55% used; 225759069 free inodes.

server3 `/tmp`: 78696763392 available bytes; 95.61% used; 114062936 free inodes.

server3 `/var/tmp`: 78696763392 available bytes; 95.61% used; 114062936 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111009464320 available bytes; 93.81% used; 114372934 free inodes.

server4 `/home`: 111009464320 available bytes; 93.81% used; 114372934 free inodes.

server4 `/data`: 382117675008 available bytes; 94.72% used; 224780554 free inodes.

server4 `/tmp`: 111009464320 available bytes; 93.81% used; 114372934 free inodes.

server4 `/var/tmp`: 111009464320 available bytes; 93.81% used; 114372934 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
