# V2R cluster inventory

2026-09-27T14:13:29.182020+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304745996288 available bytes; 83.00% used; 112401345 free inodes.

server1 `/home`: 304745996288 available bytes; 83.00% used; 112401345 free inodes.

server1 `/tmp`: 304745996288 available bytes; 83.00% used; 112401345 free inodes.

server1 `/var/tmp`: 304745996288 available bytes; 83.00% used; 112401345 free inodes.

server1 `/mnt/raid5`: 630251659264 available bytes; 97.11% used; 337424096 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13405782016 available bytes; 99.25% used; 110351806 free inodes.

server2 `/home`: 13405782016 available bytes; 99.25% used; 110351806 free inodes.

server2 `/tmp`: 13405782016 available bytes; 99.25% used; 110351806 free inodes.

server2 `/var/tmp`: 13405782016 available bytes; 99.25% used; 110351806 free inodes.

server2 `/mnt/raid5`: 527287455744 available bytes; 96.36% used; 444722914 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78558380032 available bytes; 95.62% used; 114062769 free inodes.

server3 `/home`: 78558380032 available bytes; 95.62% used; 114062769 free inodes.

server3 `/data`: 1328737054720 available bytes; 81.64% used; 225757043 free inodes.

server3 `/tmp`: 78558380032 available bytes; 95.62% used; 114062769 free inodes.

server3 `/var/tmp`: 78558380032 available bytes; 95.62% used; 114062769 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110995886080 available bytes; 93.81% used; 114372784 free inodes.

server4 `/home`: 110995886080 available bytes; 93.81% used; 114372784 free inodes.

server4 `/data`: 350752444416 available bytes; 95.15% used; 224727391 free inodes.

server4 `/tmp`: 110995886080 available bytes; 93.81% used; 114372784 free inodes.

server4 `/var/tmp`: 110995886080 available bytes; 93.81% used; 114372784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
