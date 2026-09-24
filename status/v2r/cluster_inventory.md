# V2R cluster inventory

2026-09-24T04:15:12.035052+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324710309888 available bytes; 81.89% used; 112493384 free inodes.

server1 `/home`: 324710309888 available bytes; 81.89% used; 112493384 free inodes.

server1 `/tmp`: 324710309888 available bytes; 81.89% used; 112493384 free inodes.

server1 `/var/tmp`: 324710309888 available bytes; 81.89% used; 112493384 free inodes.

server1 `/mnt/raid5`: 431145922560 available bytes; 98.02% used; 337724746 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40797896704 available bytes; 97.72% used; 110430762 free inodes.

server2 `/home`: 40797896704 available bytes; 97.72% used; 110430762 free inodes.

server2 `/tmp`: 40797896704 available bytes; 97.72% used; 110430762 free inodes.

server2 `/var/tmp`: 40797896704 available bytes; 97.72% used; 110430762 free inodes.

server2 `/mnt/raid5`: 525830574080 available bytes; 96.37% used; 445196413 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292028624896 available bytes; 83.70% used; 114176985 free inodes.

server3 `/home`: 292028624896 available bytes; 83.70% used; 114176985 free inodes.

server3 `/data`: 31722942464 available bytes; 99.56% used; 225841770 free inodes.

server3 `/tmp`: 292028624896 available bytes; 83.70% used; 114176985 free inodes.

server3 `/var/tmp`: 292028624896 available bytes; 83.70% used; 114176985 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105790562304 available bytes; 94.10% used; 114349457 free inodes.

server4 `/home`: 105790562304 available bytes; 94.10% used; 114349457 free inodes.

server4 `/data`: 256712818688 available bytes; 96.45% used; 225381824 free inodes.

server4 `/tmp`: 105790562304 available bytes; 94.10% used; 114349457 free inodes.

server4 `/var/tmp`: 105790562304 available bytes; 94.10% used; 114349457 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
