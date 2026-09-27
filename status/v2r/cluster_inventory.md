# V2R cluster inventory

2026-09-27T05:09:24.757096+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314761363456 available bytes; 82.44% used; 112442996 free inodes.

server1 `/home`: 314761363456 available bytes; 82.44% used; 112442996 free inodes.

server1 `/tmp`: 314761363456 available bytes; 82.44% used; 112442996 free inodes.

server1 `/var/tmp`: 314761363456 available bytes; 82.44% used; 112442996 free inodes.

server1 `/mnt/raid5`: 634730799104 available bytes; 97.09% used; 337400249 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17622790144 available bytes; 99.02% used; 110364996 free inodes.

server2 `/home`: 17622790144 available bytes; 99.02% used; 110364996 free inodes.

server2 `/tmp`: 17622790144 available bytes; 99.02% used; 110364996 free inodes.

server2 `/var/tmp`: 17622790144 available bytes; 99.02% used; 110364996 free inodes.

server2 `/mnt/raid5`: 575700307968 available bytes; 96.02% used; 444878416 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78576025600 available bytes; 95.62% used; 114062911 free inodes.

server3 `/home`: 78576025600 available bytes; 95.62% used; 114062911 free inodes.

server3 `/data`: 1332957708288 available bytes; 81.58% used; 225758227 free inodes.

server3 `/tmp`: 78576025600 available bytes; 95.62% used; 114062911 free inodes.

server3 `/var/tmp`: 78576025600 available bytes; 95.62% used; 114062911 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111000289280 available bytes; 93.81% used; 114372916 free inodes.

server4 `/home`: 111000289280 available bytes; 93.81% used; 114372916 free inodes.

server4 `/data`: 382066089984 available bytes; 94.72% used; 224778188 free inodes.

server4 `/tmp`: 111000289280 available bytes; 93.81% used; 114372916 free inodes.

server4 `/var/tmp`: 111000289280 available bytes; 93.81% used; 114372916 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
