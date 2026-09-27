# V2R cluster inventory

2026-09-27T13:10:52.815378+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304673656832 available bytes; 83.00% used; 112401389 free inodes.

server1 `/home`: 304673656832 available bytes; 83.00% used; 112401389 free inodes.

server1 `/tmp`: 304673656832 available bytes; 83.00% used; 112401389 free inodes.

server1 `/var/tmp`: 304673656832 available bytes; 83.00% used; 112401389 free inodes.

server1 `/mnt/raid5`: 634595491840 available bytes; 97.09% used; 337424232 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13420191744 available bytes; 99.25% used; 110351846 free inodes.

server2 `/home`: 13420191744 available bytes; 99.25% used; 110351846 free inodes.

server2 `/tmp`: 13420191744 available bytes; 99.25% used; 110351846 free inodes.

server2 `/var/tmp`: 13420191744 available bytes; 99.25% used; 110351846 free inodes.

server2 `/mnt/raid5`: 529207582720 available bytes; 96.34% used; 444733874 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78576132096 available bytes; 95.62% used; 114062842 free inodes.

server3 `/home`: 78576132096 available bytes; 95.62% used; 114062842 free inodes.

server3 `/data`: 1331498442752 available bytes; 81.60% used; 225757788 free inodes.

server3 `/tmp`: 78576132096 available bytes; 95.62% used; 114062842 free inodes.

server3 `/var/tmp`: 78576132096 available bytes; 95.62% used; 114062842 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111010906112 available bytes; 93.81% used; 114372799 free inodes.

server4 `/home`: 111010906112 available bytes; 93.81% used; 114372799 free inodes.

server4 `/data`: 351610314752 available bytes; 95.14% used; 224727807 free inodes.

server4 `/tmp`: 111010906112 available bytes; 93.81% used; 114372799 free inodes.

server4 `/var/tmp`: 111010906112 available bytes; 93.81% used; 114372799 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
