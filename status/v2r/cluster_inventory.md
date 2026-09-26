# V2R cluster inventory

2026-09-26T04:20:13.372746+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318410592256 available bytes; 82.24% used; 112476274 free inodes.

server1 `/home`: 318410592256 available bytes; 82.24% used; 112476274 free inodes.

server1 `/tmp`: 318410592256 available bytes; 82.24% used; 112476274 free inodes.

server1 `/var/tmp`: 318410592256 available bytes; 82.24% used; 112476274 free inodes.

server1 `/mnt/raid5`: 330540498944 available bytes; 98.48% used; 337545512 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22939521024 available bytes; 98.72% used; 110406205 free inodes.

server2 `/home`: 22939521024 available bytes; 98.72% used; 110406205 free inodes.

server2 `/tmp`: 22939521024 available bytes; 98.72% used; 110406205 free inodes.

server2 `/var/tmp`: 22939521024 available bytes; 98.72% used; 110406205 free inodes.

server2 `/mnt/raid5`: 285775024128 available bytes; 98.03% used; 445050668 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84145057792 available bytes; 95.30% used; 114148307 free inodes.

server3 `/home`: 84145057792 available bytes; 95.30% used; 114148307 free inodes.

server3 `/data`: 124582801408 available bytes; 98.28% used; 225819686 free inodes.

server3 `/tmp`: 84145057792 available bytes; 95.30% used; 114148307 free inodes.

server3 `/var/tmp`: 84145057792 available bytes; 95.30% used; 114148307 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002714624 available bytes; 94.08% used; 114348202 free inodes.

server4 `/home`: 106002714624 available bytes; 94.08% used; 114348202 free inodes.

server4 `/data`: 107388080128 available bytes; 98.52% used; 224929404 free inodes.

server4 `/tmp`: 106002714624 available bytes; 94.08% used; 114348202 free inodes.

server4 `/var/tmp`: 106002714624 available bytes; 94.08% used; 114348202 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
