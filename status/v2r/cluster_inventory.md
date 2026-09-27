# V2R cluster inventory

2026-09-27T12:23:36.542817+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304682532864 available bytes; 83.00% used; 112401418 free inodes.

server1 `/home`: 304682532864 available bytes; 83.00% used; 112401418 free inodes.

server1 `/tmp`: 304682532864 available bytes; 83.00% used; 112401418 free inodes.

server1 `/var/tmp`: 304682532864 available bytes; 83.00% used; 112401418 free inodes.

server1 `/mnt/raid5`: 634595106816 available bytes; 97.09% used; 337424237 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 13440122880 available bytes; 99.25% used; 110352847 free inodes.

server2 `/home`: 13440122880 available bytes; 99.25% used; 110352847 free inodes.

server2 `/tmp`: 13440122880 available bytes; 99.25% used; 110352847 free inodes.

server2 `/var/tmp`: 13440122880 available bytes; 99.25% used; 110352847 free inodes.

server2 `/mnt/raid5`: 567590215680 available bytes; 96.08% used; 444735050 free inodes.
| server3 | True | ['0', '2'] | [] | reference_compatible=True |

server3 `/`: 78547165184 available bytes; 95.62% used; 114062865 free inodes.

server3 `/home`: 78547165184 available bytes; 95.62% used; 114062865 free inodes.

server3 `/data`: 1331767214080 available bytes; 81.59% used; 225758344 free inodes.

server3 `/tmp`: 78547165184 available bytes; 95.62% used; 114062865 free inodes.

server3 `/var/tmp`: 78547165184 available bytes; 95.62% used; 114062865 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111020388352 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111020388352 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352393805824 available bytes; 95.13% used; 224727909 free inodes.

server4 `/tmp`: 111020388352 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111020388352 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
