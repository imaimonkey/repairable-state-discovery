# V2R cluster inventory

2026-09-26T03:05:25.748647+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318417956864 available bytes; 82.24% used; 112476271 free inodes.

server1 `/home`: 318417956864 available bytes; 82.24% used; 112476271 free inodes.

server1 `/tmp`: 318417956864 available bytes; 82.24% used; 112476271 free inodes.

server1 `/var/tmp`: 318417956864 available bytes; 82.24% used; 112476271 free inodes.

server1 `/mnt/raid5`: 331070435328 available bytes; 98.48% used; 337545939 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22939729920 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22939729920 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22939729920 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22939729920 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 287407710208 available bytes; 98.01% used; 445053275 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84308275200 available bytes; 95.30% used; 114152370 free inodes.

server3 `/home`: 84308275200 available bytes; 95.30% used; 114152370 free inodes.

server3 `/data`: 125442453504 available bytes; 98.27% used; 225831087 free inodes.

server3 `/tmp`: 84308275200 available bytes; 95.30% used; 114152370 free inodes.

server3 `/var/tmp`: 84308275200 available bytes; 95.30% used; 114152370 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105885085696 available bytes; 94.09% used; 114347061 free inodes.

server4 `/home`: 105885085696 available bytes; 94.09% used; 114347061 free inodes.

server4 `/data`: 109658152960 available bytes; 98.48% used; 224915263 free inodes.

server4 `/tmp`: 105885085696 available bytes; 94.09% used; 114347061 free inodes.

server4 `/var/tmp`: 105885085696 available bytes; 94.09% used; 114347061 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
