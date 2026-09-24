# V2R cluster inventory

2026-09-24T01:26:08.605942+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325464969216 available bytes; 81.84% used; 112499710 free inodes.

server1 `/home`: 325464969216 available bytes; 81.84% used; 112499710 free inodes.

server1 `/tmp`: 325464969216 available bytes; 81.84% used; 112499710 free inodes.

server1 `/var/tmp`: 325464969216 available bytes; 81.84% used; 112499710 free inodes.

server1 `/mnt/raid5`: 912576397312 available bytes; 95.81% used; 337734018 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40951422976 available bytes; 97.72% used; 110432027 free inodes.

server2 `/home`: 40951422976 available bytes; 97.72% used; 110432027 free inodes.

server2 `/tmp`: 40951422976 available bytes; 97.72% used; 110432027 free inodes.

server2 `/var/tmp`: 40951422976 available bytes; 97.72% used; 110432027 free inodes.

server2 `/mnt/raid5`: 531082776576 available bytes; 96.33% used; 445201750 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292346097664 available bytes; 83.69% used; 114187452 free inodes.

server3 `/home`: 292346097664 available bytes; 83.69% used; 114187452 free inodes.

server3 `/data`: 82045497344 available bytes; 98.87% used; 225842353 free inodes.

server3 `/tmp`: 292346097664 available bytes; 83.69% used; 114187452 free inodes.

server3 `/var/tmp`: 292346097664 available bytes; 83.69% used; 114187452 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105971499008 available bytes; 94.09% used; 114348896 free inodes.

server4 `/home`: 105971499008 available bytes; 94.09% used; 114348896 free inodes.

server4 `/data`: 290824417280 available bytes; 95.98% used; 225396990 free inodes.

server4 `/tmp`: 105971499008 available bytes; 94.09% used; 114348896 free inodes.

server4 `/var/tmp`: 105971499008 available bytes; 94.09% used; 114348896 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
