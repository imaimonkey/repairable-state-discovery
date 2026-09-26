# V2R cluster inventory

2026-09-26T03:02:22.630982+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318416871424 available bytes; 82.24% used; 112476267 free inodes.

server1 `/home`: 318416871424 available bytes; 82.24% used; 112476267 free inodes.

server1 `/tmp`: 318416871424 available bytes; 82.24% used; 112476267 free inodes.

server1 `/var/tmp`: 318416871424 available bytes; 82.24% used; 112476267 free inodes.

server1 `/mnt/raid5`: 331076894720 available bytes; 98.48% used; 337545950 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940758016 available bytes; 98.72% used; 110406214 free inodes.

server2 `/home`: 22940758016 available bytes; 98.72% used; 110406214 free inodes.

server2 `/tmp`: 22940758016 available bytes; 98.72% used; 110406214 free inodes.

server2 `/var/tmp`: 22940758016 available bytes; 98.72% used; 110406214 free inodes.

server2 `/mnt/raid5`: 288030339072 available bytes; 98.01% used; 445053394 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84308885504 available bytes; 95.30% used; 114152370 free inodes.

server3 `/home`: 84308885504 available bytes; 95.30% used; 114152370 free inodes.

server3 `/data`: 125440778240 available bytes; 98.27% used; 225831164 free inodes.

server3 `/tmp`: 84308885504 available bytes; 95.30% used; 114152370 free inodes.

server3 `/var/tmp`: 84308885504 available bytes; 95.30% used; 114152370 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105885200384 available bytes; 94.09% used; 114347063 free inodes.

server4 `/home`: 105885200384 available bytes; 94.09% used; 114347063 free inodes.

server4 `/data`: 109661249536 available bytes; 98.48% used; 224915308 free inodes.

server4 `/tmp`: 105885200384 available bytes; 94.09% used; 114347063 free inodes.

server4 `/var/tmp`: 105885200384 available bytes; 94.09% used; 114347063 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
