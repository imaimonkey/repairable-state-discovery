# V2R cluster inventory

2026-09-27T05:07:53.379154+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314796777472 available bytes; 82.44% used; 112442997 free inodes.

server1 `/home`: 314796777472 available bytes; 82.44% used; 112442997 free inodes.

server1 `/tmp`: 314796777472 available bytes; 82.44% used; 112442997 free inodes.

server1 `/var/tmp`: 314796777472 available bytes; 82.44% used; 112442997 free inodes.

server1 `/mnt/raid5`: 634727325696 available bytes; 97.09% used; 337400248 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17623396352 available bytes; 99.02% used; 110364998 free inodes.

server2 `/home`: 17623396352 available bytes; 99.02% used; 110364998 free inodes.

server2 `/tmp`: 17623396352 available bytes; 99.02% used; 110364998 free inodes.

server2 `/var/tmp`: 17623396352 available bytes; 99.02% used; 110364998 free inodes.

server2 `/mnt/raid5`: 575734231040 available bytes; 96.02% used; 444878321 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78610866176 available bytes; 95.61% used; 114062912 free inodes.

server3 `/home`: 78610866176 available bytes; 95.61% used; 114062912 free inodes.

server3 `/data`: 1333586755584 available bytes; 81.57% used; 225758263 free inodes.

server3 `/tmp`: 78610866176 available bytes; 95.61% used; 114062912 free inodes.

server3 `/var/tmp`: 78610866176 available bytes; 95.61% used; 114062912 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111000334336 available bytes; 93.81% used; 114372918 free inodes.

server4 `/home`: 111000334336 available bytes; 93.81% used; 114372918 free inodes.

server4 `/data`: 382068568064 available bytes; 94.72% used; 224778196 free inodes.

server4 `/tmp`: 111000334336 available bytes; 93.81% used; 114372918 free inodes.

server4 `/var/tmp`: 111000334336 available bytes; 93.81% used; 114372918 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
