# V2R cluster inventory

2026-09-27T04:55:42.390919+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314887307264 available bytes; 82.43% used; 112443018 free inodes.

server1 `/home`: 314887307264 available bytes; 82.43% used; 112443018 free inodes.

server1 `/tmp`: 314887307264 available bytes; 82.43% used; 112443018 free inodes.

server1 `/var/tmp`: 314887307264 available bytes; 82.43% used; 112443018 free inodes.

server1 `/mnt/raid5`: 636047761408 available bytes; 97.08% used; 337400299 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17620541440 available bytes; 99.02% used; 110365002 free inodes.

server2 `/home`: 17620541440 available bytes; 99.02% used; 110365002 free inodes.

server2 `/tmp`: 17620541440 available bytes; 99.02% used; 110365002 free inodes.

server2 `/var/tmp`: 17620541440 available bytes; 99.02% used; 110365002 free inodes.

server2 `/mnt/raid5`: 575551700992 available bytes; 96.02% used; 444878520 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78694354944 available bytes; 95.61% used; 114062918 free inodes.

server3 `/home`: 78694354944 available bytes; 95.61% used; 114062918 free inodes.

server3 `/data`: 1333985996800 available bytes; 81.56% used; 225758810 free inodes.

server3 `/tmp`: 78694354944 available bytes; 95.61% used; 114062918 free inodes.

server3 `/var/tmp`: 78694354944 available bytes; 95.61% used; 114062918 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111000649728 available bytes; 93.81% used; 114372922 free inodes.

server4 `/home`: 111000649728 available bytes; 93.81% used; 114372922 free inodes.

server4 `/data`: 382105079808 available bytes; 94.72% used; 224780470 free inodes.

server4 `/tmp`: 111000649728 available bytes; 93.81% used; 114372922 free inodes.

server4 `/var/tmp`: 111000649728 available bytes; 93.81% used; 114372922 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
