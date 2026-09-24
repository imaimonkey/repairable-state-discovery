# V2R cluster inventory

2026-09-24T02:42:21.359559+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325383802880 available bytes; 81.85% used; 112498750 free inodes.

server1 `/home`: 325383802880 available bytes; 81.85% used; 112498750 free inodes.

server1 `/tmp`: 325383802880 available bytes; 81.85% used; 112498750 free inodes.

server1 `/var/tmp`: 325383802880 available bytes; 81.85% used; 112498750 free inodes.

server1 `/mnt/raid5`: 594649563136 available bytes; 97.27% used; 337733168 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40877449216 available bytes; 97.72% used; 110431448 free inodes.

server2 `/home`: 40877449216 available bytes; 97.72% used; 110431448 free inodes.

server2 `/tmp`: 40877449216 available bytes; 97.72% used; 110431448 free inodes.

server2 `/var/tmp`: 40877449216 available bytes; 97.72% used; 110431448 free inodes.

server2 `/mnt/raid5`: 528633798656 available bytes; 96.35% used; 445199151 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292667170816 available bytes; 83.67% used; 114209071 free inodes.

server3 `/home`: 292667170816 available bytes; 83.67% used; 114209071 free inodes.

server3 `/data`: 39735775232 available bytes; 99.45% used; 225846078 free inodes.

server3 `/tmp`: 292667170816 available bytes; 83.67% used; 114209071 free inodes.

server3 `/var/tmp`: 292667170816 available bytes; 83.67% used; 114209071 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106003099648 available bytes; 94.08% used; 114349830 free inodes.

server4 `/home`: 106003099648 available bytes; 94.08% used; 114349830 free inodes.

server4 `/data`: 289734295552 available bytes; 96.00% used; 225387275 free inodes.

server4 `/tmp`: 106003099648 available bytes; 94.08% used; 114349830 free inodes.

server4 `/var/tmp`: 106003099648 available bytes; 94.08% used; 114349830 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
